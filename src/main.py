from __future__ import annotations

from pathlib import Path
import sqlite3
import pandas as pd

from src.screener.engine import load_config, score_snapshot, preset
from src.analytics.peer import build_peer_percentiles, load_peer_groups
from src.reports.excel_reports import export_peer, export_screener
from src.reports.radar import generate_radar_charts

ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/"data"; OUT=ROOT/"output"; REPORTS=ROOT/"reports"; CONFIG=ROOT/"config/screener_config.yaml"


def run():
    OUT.mkdir(exist_ok=True)
    (REPORTS/"radar_charts").mkdir(parents=True,exist_ok=True)
    df=pd.read_csv(DATA/"n100_financials.csv")
    pg=load_peer_groups(DATA/"peer_groups.xlsx")
    config=load_config(CONFIG)
    scored=score_snapshot(df,CONFIG)
    presets={name:preset(scored,name,CONFIG) for name in config["presets"]}
    counts={k:len(v) for k,v in presets.items()}
    print("Preset counts:",counts)
    bad={k:v for k,v in counts.items() if not 5<=v<=50}
    if bad:
        raise RuntimeError(f"Preset counts outside 5..50: {bad}")
    export_screener(scored,presets,OUT/"screener_output.xlsx",config)
    pct=build_peer_percentiles(scored,pg,OUT/"screener.sqlite",year=2024)
    export_peer(scored,pct,pg,OUT/"peer_comparison.xlsx")
    generate_radar_charts(scored,pct,REPORTS/"radar_charts")
    with sqlite3.connect(OUT/"screener.sqlite") as con:
        n=con.execute("select count(*) from peer_percentiles").fetchone()[0]
    print("Peer percentile records:",n)
    print("Radar charts:",len(list((REPORTS/"radar_charts").glob("*_radar.png"))))


if __name__=="__main__":
    run()
