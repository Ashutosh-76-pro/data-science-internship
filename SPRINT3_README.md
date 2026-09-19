# Sprint 3 — Screener & Peer Comparison Engine

This branch implements the complete Sprint 3 deliverable for the financial intelligence project.

## What is included

- Config-driven screener engine with all 15 requested filterable metrics and six presets.
- Financials-sector D/E exemption and `Debt Free` → infinite ICR handling.
- Sector-relative P10/P90 winsorised composite quality score on a 0–100 scale.
- Peer percentile engine for 11 peer groups × 10 metrics with inverse D/E ranking.
- SQLite `peer_percentiles` table with 920 records for the 92-company demo universe.
- Colour-coded `screener_output.xlsx` with six preset sheets.
- Colour-coded `peer_comparison.xlsx` with 11 peer-group sheets and median summary rows.
- 92 company radar charts under `reports/radar_charts/`.
- 14 Sprint 3 DQ unit tests.

## Run

```bash
pip install -r requirements-sprint3.txt
PYTHONPATH=. python -m src.main
PYTHONPATH=. pytest -q tests/test_sprint3.py
```

## Demo data note

The repository branch uses a **synthetic 92-company Nifty-100-style demo dataset** so all outputs are reproducible and runnable. It is not presented as live or authoritative market data. Replace `data/n100_financials.csv` and `data/peer_groups.xlsx` with the validated upstream Sprint 1/2 datasets when those files are available.

## Sprint deliverables

```text
config/screener_config.yaml
src/screener/engine.py
src/analytics/peer.py
src/reports/excel_reports.py
src/reports/radar.py
output/screener_output.xlsx
output/peer_comparison.xlsx
output/screener.sqlite
reports/radar_charts/*_radar.png
```
