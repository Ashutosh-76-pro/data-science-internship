# Sprint 3 — Validation Evidence

## Generation
- Input universe: 92 unique companies.
- Presets: 6.
- Peer groups: 11.
- Peer metrics: 10.
- Peer percentile records: 920 (92 × 10).
- Radar charts: 92 PNG files.

## Preset counts
| Preset | Companies |
|---|---:|
| Quality Compounder | 28 |
| Value Pick | 20 |
| Growth Accelerator | 15 |
| Dividend Champion | 18 |
| Debt Free Bluechip | 44 |
| Turnaround Watch | 15 |

All six preset counts are within the required 5–50 range.

## Report structure
- output/screener_output.xlsx: exactly 6 sheets.
- output/peer_comparison.xlsx: exactly 11 sheets.
- Screener sheets contain the requested 20 KPI columns.
- Peer report includes percentile columns, benchmark-row highlighting, and peer-median summary rows.
- output/screener.sqlite contains peer_percentiles with 920 rows.

## DQ validation

Command: PYTHONPATH=. pytest -q tests/test_sprint3.py

Result: 14 passed, 0 failed.

The 14 checks cover universe size, filter configuration, all presets, D/E Financials exemption, Debt Free → infinite ICR, score bounds, peer-group completeness, all ten metrics, percentile count/range, IT Services ROE spot-check, Excel sheet counts, and SQLite row count.

## Data note
The branch uses a synthetic 92-company Nifty-100-style demo dataset for reproducibility. It is not presented as live or authoritative market data. Replace it with the validated Sprint 1/2 upstream dataset when available; the Sprint 3 engine and report format remain unchanged.