from __future__ import annotations

from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

AXES = ["ROE", "ROCE", "NPM", "D/E", "FCF Score", "PAT CAGR 5Y", "Revenue CAGR 5Y", "Composite Score"]
SOURCE = ["roe_pct","roce_pct","npm_pct","debt_to_equity","fcf_cr","pat_cagr_5y_pct","revenue_cagr_5y_pct","composite_quality_score"]


def _scale_group(s: pd.Series, inverse: bool=False) -> pd.Series:
    x=pd.to_numeric(s,errors="coerce").replace([np.inf,-np.inf],np.nan)
    lo,hi=x.min(),x.max()
    if pd.isna(lo) or hi==lo: out=pd.Series(50.0,index=s.index)
    else: out=(x-lo)/(hi-lo)*100
    if inverse: out=100-out
    return out.fillna(50).clip(0,100)


def generate_radar_charts(df: pd.DataFrame, percentiles: pd.DataFrame, output_dir: str | Path):
    out=Path(output_dir); out.mkdir(parents=True,exist_ok=True)
    for group,gdf in df.groupby("peer_group_name"):
        scaled={
            "roe_pct":_scale_group(gdf["roe_pct"]),"roce_pct":_scale_group(gdf["roce_pct"]),"npm_pct":_scale_group(gdf["npm_pct"]),
            "debt_to_equity":_scale_group(gdf["debt_to_equity"],True),
            "fcf_cr":_scale_group(gdf["fcf_cr"]),"pat_cagr_5y_pct":_scale_group(gdf["pat_cagr_5y_pct"]),
            "revenue_cagr_5y_pct":_scale_group(gdf["revenue_cagr_5y_pct"]),"composite_quality_score":gdf["composite_quality_score"].clip(0,100)
        }
        peer_avg=[float(pd.Series(scaled[k]).mean()) for k in SOURCE]
        angles=np.linspace(0,2*np.pi,len(AXES),endpoint=False).tolist(); angles+=angles[:1]
        for ix,row in gdf.iterrows():
            vals=[float(scaled[k].loc[ix]) for k in SOURCE]; vals+=vals[:1]
            fig=plt.figure(figsize=(7.2,7.2)); ax=fig.add_subplot(111,polar=True)
            ax.plot(angles,vals,linewidth=2); ax.fill(angles,vals,alpha=0.20)
            avg=peer_avg+[peer_avg[0]]; ax.plot(angles,avg,linewidth=2,linestyle="--")
            ax.set_thetagrids(np.degrees(angles[:-1]),AXES,fontsize=10)
            ax.set_ylim(0,100); ax.set_yticks([20,40,60,80,100]); ax.set_yticklabels(["20","40","60","80","100"],fontsize=8)
            ax.set_title(f"{row.company_id} — {group}\nCompany vs Peer Group Average",fontsize=13,pad=20)
            ax.legend(["Company","Peer Average"],loc="upper right",bbox_to_anchor=(1.25,1.1),fontsize=9)
            fig.tight_layout(); fig.savefig(out/f"{row.company_id}_radar.png",dpi=160,bbox_inches="tight"); plt.close(fig)
    unassigned = df[df["peer_group_name"].isna()] if "peer_group_name" in df.columns else df.copy()
    if not unassigned.empty:
        universe_average = float(pd.to_numeric(df["composite_quality_score"], errors="coerce").mean())
        for _, row in unassigned.iterrows():
            fig=plt.figure(figsize=(6.5,5.5)); ax=fig.add_subplot(111)
            company=float(pd.to_numeric(pd.Series([row["composite_quality_score"]]), errors="coerce").iloc[0])
            ax.bar(["Composite Score"],[company])
            ax.axhline(universe_average, linestyle="--", linewidth=2, label="Nifty 100 average")
            ax.set_ylim(0,100); ax.set_ylabel("Score (0–100)")
            ax.set_title(f"{row.company_id} — No peer group assigned", fontsize=13)
            ax.legend(fontsize=9); fig.tight_layout()
            fig.savefig(out/f"{row.company_id}_radar.png",dpi=160,bbox_inches="tight"); plt.close(fig)
