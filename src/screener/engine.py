from __future__ import annotations

from pathlib import Path
from typing import Any, Mapping
import math

import numpy as np
import pandas as pd
import yaml

DEFAULT_CONFIG = Path(__file__).resolve().parents[2] / "config" / "screener_config.yaml"

DISPLAY_KPI_COLUMNS = [
    "roe_pct","roce_pct","npm_pct","opm_pct","debt_to_equity","interest_coverage","fcf_cr",
    "fcf_cagr_5y_pct","cfo_pat_ratio","revenue_cagr_5y_pct","pat_cagr_5y_pct","eps_cagr_5y_pct",
    "asset_turnover","pe","pb","dividend_yield_pct","dividend_payout_pct","market_cap_cr","net_profit_cr","sales_cr",
]

FILTERABLE_METRICS = [
    "roe_pct","debt_to_equity","fcf_cr","revenue_cagr_5y_pct","pat_cagr_5y_pct","opm_pct","pe","pb",
    "dividend_yield_pct","interest_coverage","market_cap_cr","net_profit_cr","eps_cagr_5y_pct","asset_turnover","sales_cr",
]

HIGHER_IS_BETTER = {
    "roe_pct": True, "roce_pct": True, "npm_pct": True, "fcf_cagr_5y_pct": True, "cfo_pat_ratio": True,
    "fcf_positive": True, "revenue_cagr_5y_pct": True, "pat_cagr_5y_pct": True, "debt_to_equity": False,
    "interest_coverage": True,
}

COLUMN_LABELS = {
    "roe_pct":"ROE (%)","roce_pct":"ROCE (%)","npm_pct":"Net Profit Margin (%)","opm_pct":"OPM (%)",
    "debt_to_equity":"D/E","interest_coverage":"ICR","fcf_cr":"FCF (₹ Cr)","fcf_cagr_5y_pct":"FCF CAGR 5Y (%)",
    "cfo_pat_ratio":"CFO/PAT","revenue_cagr_5y_pct":"Revenue CAGR 5Y (%)","pat_cagr_5y_pct":"PAT CAGR 5Y (%)",
    "eps_cagr_5y_pct":"EPS CAGR 5Y (%)","asset_turnover":"Asset Turnover","pe":"P/E","pb":"P/B",
    "dividend_yield_pct":"Dividend Yield (%)","dividend_payout_pct":"Dividend Payout (%)","market_cap_cr":"Market Cap (₹ Cr)",
    "net_profit_cr":"Net Profit (₹ Cr)","sales_cr":"Sales (₹ Cr)","revenue_cagr_3y_pct":"Revenue CAGR 3Y (%)","de_yoy_change":"D/E YoY Change",
    "fcf_positive":"FCF Positive Flag",
}


def load_config(path: str | Path = DEFAULT_CONFIG) -> dict[str, Any]:
    with Path(path).open("r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def _numeric_series(series: pd.Series) -> pd.Series:
    if series.dtype == object:
        s = series.astype("string").str.strip().str.lower()
        result = pd.to_numeric(s, errors="coerce")
        result = result.mask(s.eq("debt free"), np.inf)
        return result
    return pd.to_numeric(series, errors="coerce")


def winsorised_percentile_score(series: pd.Series, higher_is_better: bool = True) -> pd.Series:
    numeric = _numeric_series(series).replace([np.inf, -np.inf], np.nan)
    valid = numeric.dropna()
    if valid.empty:
        return pd.Series(50.0, index=series.index)
    p10, p90 = valid.quantile([0.10, 0.90]).tolist()
    if math.isclose(p10, p90):
        return pd.Series(50.0, index=series.index)
    clipped = numeric.clip(p10, p90)
    score = (clipped - p10) / (p90 - p10) * 100.0
    if not higher_is_better:
        score = 100.0 - score
    median = float(score.median()) if score.notna().any() else 50.0
    return score.fillna(median).clip(0, 100)


def sector_relative_score(series: pd.Series, sectors: pd.Series, higher_is_better: bool = True) -> pd.Series:
    out = pd.Series(index=series.index, dtype=float)
    for sector, idx in sectors.groupby(sectors).groups.items():
        out.loc[idx] = winsorised_percentile_score(series.loc[idx], higher_is_better)
    return out.fillna(50.0).clip(0, 100)


def add_composite_quality_score(df: pd.DataFrame) -> pd.DataFrame:
    result = df.copy()
    required = {"broad_sector", "roe_pct", "roce_pct", "npm_pct", "fcf_cagr_5y_pct", "cfo_pat_ratio", "fcf_positive",
                "revenue_cagr_5y_pct", "pat_cagr_5y_pct", "debt_to_equity", "interest_coverage"}
    missing = required - set(result.columns)
    if missing:
        raise ValueError(f"Composite score missing columns: {sorted(missing)}")
    components = {}
    for metric in ["roe_pct","roce_pct","npm_pct","fcf_cagr_5y_pct","cfo_pat_ratio","revenue_cagr_5y_pct","pat_cagr_5y_pct","debt_to_equity","interest_coverage"]:
        components[metric] = sector_relative_score(result[metric], result["broad_sector"], HIGHER_IS_BETTER[metric])
    components["fcf_positive"] = _numeric_series(result["fcf_positive"]).fillna(0).clip(0,1)*100
    result["profitability_score"] = (components["roe_pct"]*.15 + components["roce_pct"]*.10 + components["npm_pct"]*.10)
    result["cash_quality_score"] = (components["fcf_cagr_5y_pct"]*.15 + components["cfo_pat_ratio"]*.10 + components["fcf_positive"]*.05)
    result["growth_score"] = (components["revenue_cagr_5y_pct"]*.10 + components["pat_cagr_5y_pct"]*.10)
    result["leverage_score"] = (components["debt_to_equity"]*.10 + components["interest_coverage"]*.05)
    result["composite_quality_score"] = (result[["profitability_score","cash_quality_score","growth_score","leverage_score"]].sum(axis=1)).round(2).clip(0,100)
    return result


def apply_thresholds(df: pd.DataFrame, thresholds: Mapping[str, Mapping[str, Any]]) -> pd.Series:
    mask = pd.Series(True, index=df.index)
    for metric, rule in thresholds.items():
        if metric not in FILTERABLE_METRICS and metric not in {"revenue_cagr_3y_pct", "de_yoy_change", "dividend_payout_pct"}:
            raise ValueError(f"Unsupported filter metric: {metric}")
        if metric not in df.columns:
            raise ValueError(f"DataFrame missing filter metric: {metric}")
        if metric == "debt_to_equity" and "broad_sector" in df.columns:
            applicable = ~df["broad_sector"].astype("string").str.casefold().eq("financials")
        else:
            applicable = pd.Series(True, index=df.index)
        values = _numeric_series(df[metric])
        op = str(rule.get("op", "min")).lower()
        target = float(rule.get("value"))
        if op in {"min", ">="}: passed = values >= target
        elif op in {"max", "<="}: passed = values <= target
        elif op in {"gt", ">"}: passed = values > target
        elif op in {"lt", "<"}: passed = values < target
        elif op in {"eq", "="}: passed = pd.Series(np.isclose(values.to_numpy(dtype=float), target, atol=1e-12, equal_nan=False), index=values.index)
        else: raise ValueError(f"Unsupported operator: {op}")
        mask &= (~applicable) | passed.fillna(False)
    return mask


def screen(df: pd.DataFrame, thresholds: Mapping[str, Mapping[str, Any]], sort_desc: bool = True) -> pd.DataFrame:
    result = add_composite_quality_score(df)
    mask = apply_thresholds(result, thresholds)
    result["passes_preset"] = mask
    filtered = result.loc[mask].copy()
    return filtered.sort_values("composite_quality_score", ascending=not sort_desc).reset_index(drop=True)


def preset(df: pd.DataFrame, preset_name: str, config_path: str | Path = DEFAULT_CONFIG) -> pd.DataFrame:
    config = load_config(config_path)
    try:
        thresholds = config["presets"][preset_name]
    except KeyError as e:
        raise KeyError(f"Unknown preset: {preset_name}") from e
    return screen(df, thresholds)


def score_snapshot(df: pd.DataFrame, config_path: str | Path = DEFAULT_CONFIG) -> pd.DataFrame:
    _ = load_config(config_path)
    return add_composite_quality_score(df)
