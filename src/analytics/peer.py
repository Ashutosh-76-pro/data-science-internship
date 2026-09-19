from __future__ import annotations

from pathlib import Path
import sqlite3
import math

import numpy as np
import pandas as pd

PEER_METRICS = {
    "roe_pct": {"higher_is_better": True, "label": "ROE"},
    "roce_pct": {"higher_is_better": True, "label": "ROCE"},
    "npm_pct": {"higher_is_better": True, "label": "Net Profit Margin"},
    "debt_to_equity": {"higher_is_better": False, "label": "D/E"},
    "fcf_cr": {"higher_is_better": True, "label": "FCF"},
    "pat_cagr_5y_pct": {"higher_is_better": True, "label": "PAT CAGR 5Y"},
    "revenue_cagr_5y_pct": {"higher_is_better": True, "label": "Revenue CAGR 5Y"},
    "eps_cagr_5y_pct": {"higher_is_better": True, "label": "EPS CAGR 5Y"},
    "interest_coverage": {"higher_is_better": True, "label": "Interest Coverage"},
    "asset_turnover": {"higher_is_better": True, "label": "Asset Turnover"},
}


def _numeric(series: pd.Series) -> pd.Series:
    s = series.astype("string").str.strip().str.lower() if series.dtype == object else series
    n = pd.to_numeric(s, errors="coerce")
    return n.mask(s.eq("debt free"), np.inf)


def percent_rank(values: pd.Series, higher_is_better: bool = True) -> pd.Series:
    numeric = _numeric(values)
    valid = numeric.dropna()
    if valid.empty:
        return pd.Series(np.nan, index=values.index, dtype=float)
    if len(valid) == 1:
        ranked = pd.Series(0.0, index=valid.index)
    else:
        ranks = valid.rank(method="min", ascending=True)
        ranked = (ranks - 1) / (len(valid) - 1)
    return ranked.reindex(values.index)


def load_peer_groups(path: str | Path) -> pd.DataFrame:
    groups = pd.read_excel(path)
    required={"company_id","peer_group_name","benchmark_company","year"}
    missing=required-set(groups.columns)
    if missing:
        raise ValueError(f"peer_groups.xlsx missing columns: {sorted(missing)}")
    return groups


def compute_peer_percentiles(df: pd.DataFrame, peer_groups: pd.DataFrame | str | Path, year: int | None = None) -> pd.DataFrame:
    groups = load_peer_groups(peer_groups) if not isinstance(peer_groups, pd.DataFrame) else peer_groups.copy()
    work = df.copy()
    if year is not None and "year" in work.columns:
        work = work.loc[work["year"].eq(year)].copy()
    merged = work.merge(groups[["company_id","peer_group_name","year"]], on="company_id", how="left", suffixes=("","_pg"))
    merged["year"] = merged["year_pg"].fillna(merged.get("year", pd.Series(index=merged.index))).astype("Int64")
    unassigned = merged[merged["peer_group_name"].isna()]
    if not unassigned.empty:
        for company_id in unassigned["company_id"].tolist():
            print(f"{company_id}: No peer group assigned")
    output=[]
    for company_group, gdf in merged.dropna(subset=["peer_group_name"]).groupby("peer_group_name", sort=True):
        for metric, meta in PEER_METRICS.items():
            if metric not in gdf.columns:
                continue
            ranks = percent_rank(gdf[metric], higher_is_better=bool(meta["higher_is_better"]))
            if metric == "debt_to_equity":
                ranks = 1.0 - ranks
            for idx in gdf.index:
                val=_numeric(pd.Series([gdf.loc[idx, metric]])).iloc[0]
                output.append({
                    "company_id":gdf.loc[idx,"company_id"],"peer_group_name":company_group,"metric":metric,
                    "value":None if pd.isna(val) else float(val),
                    "percentile_rank":None if pd.isna(ranks.loc[idx]) else round(float(ranks.loc[idx]),6),
                    "year":int(gdf.loc[idx,"year"] if pd.notna(gdf.loc[idx,"year"]) else year or 2024),
                })
    return pd.DataFrame(output, columns=["company_id","peer_group_name","metric","value","percentile_rank","year"])


def persist_peer_percentiles(records: pd.DataFrame, db_path: str | Path) -> None:
    db=Path(db_path); db.parent.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(db) as con:
        con.execute("""CREATE TABLE IF NOT EXISTS peer_percentiles (
            company_id TEXT NOT NULL,
            peer_group_name TEXT NOT NULL,
            metric TEXT NOT NULL,
            value REAL,
            percentile_rank REAL,
            year INTEGER NOT NULL,
            PRIMARY KEY(company_id, peer_group_name, metric, year)
        )""")
        con.execute("CREATE INDEX IF NOT EXISTS idx_peer_percentiles_group_metric ON peer_percentiles(peer_group_name, metric)")
        con.execute("DELETE FROM peer_percentiles")
        records.to_sql("peer_percentiles", con, if_exists="append", index=False)


def build_peer_percentiles(df: pd.DataFrame, peer_groups: pd.DataFrame | str | Path, db_path: str | Path, year: int = 2024) -> pd.DataFrame:
    records=compute_peer_percentiles(df, peer_groups, year=year)
    persist_peer_percentiles(records, db_path)
    return records
