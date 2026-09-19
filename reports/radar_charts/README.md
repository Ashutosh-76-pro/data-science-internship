# Sprint 3 radar charts

The radar generator creates one *_radar.png per company.

Peer-group charts use 8 axes: ROE, ROCE, Net Profit Margin, D/E, FCF Score, PAT CAGR 5Y, Revenue CAGR 5Y, and Composite Score.

Each chart overlays the company polygon with a dashed peer-group-average outline. Companies without an assigned peer group receive a standalone reference chart.

Regenerate with: PYTHONPATH=. python -m src.main