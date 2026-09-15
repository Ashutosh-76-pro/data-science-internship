# Data Analyst Prerequisite — 14-Day Project-Ready Track

This folder contains a complete self-paced preparation track based on the provided 2-week Data Analyst prerequisite requirements.

## Goal
Build enough technical, analytical, business, and communication skill to independently complete a practical Data Analyst assessment and become project-ready.

## 14-Day flow

| Day | Focus | Practical output |
|---|---|---|
| 1 | Data Analytics fundamentals | Analyst role + analytics lifecycle notes |
| 2 | Business thinking, KPIs & metrics | KPI dictionary + business questions |
| 3 | Excel fundamentals | Formula and data-cleaning practice |
| 4 | Excel analysis | Pivot-style analysis + chart plan |
| 5 | SQL fundamentals | Filtering, grouping, joins, CASE |
| 6 | Advanced SQL | CTEs, subqueries, window functions |
| 7 | Python + Pandas + statistics | Data profiling script |
| 8 | Data cleaning | Missing values, duplicates, outliers |
| 9 | EDA | Trends, distributions, segments, anomalies |
| 10 | Power BI | Data model + dashboard wireframe |
| 11 | DAX | KPI measures and comparison measures |
| 12 | Visualisation + storytelling | Insight narrative and recommendation |
| 13 | End-to-end mock project | Business analysis using the sample dataset |
| 14 | Prerequisite assessment | Timed theory + SQL + Python + case study |

## Repository structure

```text
data-analyst-prerequisite/
├── README.md
├── 14_DAY_PLAN.md
├── data/
│   └── sales_data.csv
├── excel/
│   └── EXCEL_PRACTICE.md
├── sql/
│   └── SQL_PRACTICE.sql
├── python/
│   └── eda_and_cleaning.py
├── powerbi/
│   └── DAX_AND_DASHBOARD.md
└── assessment/
    └── PREREQUISITE_ASSESSMENT.md
```

## Main capstone

The practical dataset is a small synthetic retail-sales dataset. It is intentionally simple enough for learning but contains missing discounts, duplicate transaction IDs, region variation, returns, and different product categories so that cleaning, SQL, Python, KPI analysis, and dashboard reasoning can all be practiced.

### Suggested business questions

1. What is total sales and net sales after returns?
2. Which regions and categories perform best?
3. Which products have high sales but weak margins?
4. How are monthly sales changing?
5. Which customer segments contribute the most revenue?
6. Where do data-quality issues affect analysis?
7. What business actions should management take next month?

## Evidence of project readiness

A strong completion should demonstrate:

- Clear definitions of metrics, dimensions, KPIs, and business questions.
- Reliable Excel calculations and basic data-cleaning ability.
- SQL queries that work without hardcoded answers.
- Python/Pandas profiling, cleaning, and EDA.
- Power BI model and dashboard thinking.
- Correct DAX measures rather than manually typed totals.
- Ability to explain what happened, what changed, why it matters, and what action is recommended.
- Independent completion of the assessment in `assessment/PREREQUISITE_ASSESSMENT.md`.

## How to run the Python practice

```bash
pip install pandas numpy matplotlib
python data-analyst-prerequisite/python/eda_and_cleaning.py
```

The script reads the included CSV, reports quality issues, cleans the data, calculates core KPIs, and produces basic EDA outputs.

## Important

This is an educational portfolio/practice module. The dataset is synthetic and should not be represented as real company performance or confidential business data.
