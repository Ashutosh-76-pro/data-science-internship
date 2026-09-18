# Assessment Readiness — Data Analyst Prerequisite

**Candidate:** Ashutosh Yadav  
**Repository:** `Ashutosh-76-pro/data-science-internship`  
**Assessment basis:** 14-day Data Analyst prerequisite

## Purpose

This document maps the repository evidence to the prerequisite assessment areas: Excel, SQL, Advanced SQL, data cleaning, statistics, Python/Pandas, EDA, Power BI, DAX, visualization, KPIs, business analytics, interpretation and practical problem solving.

## Evidence map

| Assessment area | Repository evidence | What is demonstrated |
|---|---|---|
| Excel | `data-analyst-prerequisite/excel/EXCEL_PRACTICE.md` | Formulas, filtering, PivotTable analysis and KPI calculations |
| SQL | `data-analyst-prerequisite/sql/SQL_PRACTICE.sql` | SELECT, filtering, grouping, HAVING, CASE, joins and data-quality checks |
| Advanced SQL | Same SQL practice file | CTEs, LAG, ranking, window functions and contribution analysis |
| Data cleaning | `data-analyst-prerequisite/python/eda_and_cleaning.py` | Missing-value treatment, duplicate handling, type standardisation and derived fields |
| Statistics | 14-day plan + Python EDA workflow | Mean, median, variance, standard deviation, percentiles, IQR and correlation concepts |
| Python / Pandas | `data-analyst-prerequisite/python/eda_and_cleaning.py` | CSV loading, profiling, transformations, groupby analysis and chart generation |
| EDA | `data-analyst-prerequisite/CAPSTONE_ANALYSIS.md` | Trends, segments, product performance, regional analysis and anomaly-oriented checks |
| Power BI | `data-analyst-prerequisite/powerbi/DAX_AND_DASHBOARD.md` | Dashboard layout, KPI cards, slicers, model and visual design |
| DAX | Same Power BI/DAX guide | Reusable measures for sales, profit, margin and returns |
| KPIs | `Documentation/DATA_DICTIONARY.md` | Metric definitions and formulas |
| Business analytics | `data-analyst-prerequisite/CAPSTONE_ANALYSIS.md` | Business questions, findings, recommendations and limitations |
| Interpretation | Capstone analysis + presentation | Evidence-backed explanation of what happened and what changed |
| Practical assessment | `data-analyst-prerequisite/assessment/PREREQUISITE_ASSESSMENT.md` | 120-minute mock test across all major sections |

## Practical readiness checklist

Before treating the prerequisite as complete, verify that you can independently:

- Load and inspect an unfamiliar dataset.
- Identify missing values, duplicates and invalid records.
- Explain the grain of the data before deduplicating.
- Calculate Gross Sales, Net Sales, Cost, Profit, Margin % and Return Rate.
- Write SQL aggregations, CASE logic, CTEs and window functions.
- Use Pandas for profiling, cleaning, grouping and EDA.
- Explain mean vs median, standard deviation, IQR and correlation vs causation.
- Design a Power BI dashboard around business questions rather than decoration.
- Write DAX measures and explain filter context.
- Turn an observation into evidence, implication and an actionable recommendation.
- State assumptions and limitations instead of presenting unsupported causal claims.

## Dataset quality checks used

The training dataset contains **41 raw rows** and **40 unique transaction IDs after removing the duplicate T020**. It also contains **one missing discount value**. Returned orders are explicitly treated as zero for Net Sales and Profit in the training analysis.

The raw dataset is preserved at:

`Datasets/sales_data.csv`

and the same dataset is used by the prerequisite module at:

`data-analyst-prerequisite/data/sales_data.csv`

## Mock-project evidence

The completed retail analysis reports:

- Gross Sales: **₹480,370**
- Net Sales: **₹450,930**
- Profit: **₹138,890**
- Profit Margin: **30.80%**
- Return Rate: **7.50%**
- March 2026 was the peak Net Sales month.
- April 2026 declined **13.50%** versus March.
- Corporate generated **₹287,880** in Net Sales.
- Monitor generated high Net Sales but had a relatively low **22.24%** product margin.

These values come from the synthetic training dataset and are not real company performance.

## Assessment-day approach

Use the following sequence during the mock test:

**Understand → Validate → Calculate → Cross-check → Interpret → Communicate**

Do not start with charts or recommendations before checking the data grain and metric definitions.

## Readiness statement

Completion of this repository demonstrates structured preparation and practical evidence. Project assignment should still depend on the actual prerequisite assessment and the organisation's required standard.
