# 14-Day Data Analyst Self-Paced Plan

## Week 1 — Foundations & Technical Skills

### Day 1 — Data Analytics Foundations
**Learn**
- What Data Analytics is and how it supports business decisions.
- Data Analyst vs Data Scientist vs Data Engineer.
- Analytics lifecycle: define → collect → clean → explore → analyze → communicate → act.
- Descriptive, diagnostic, predictive, and prescriptive analytics.
- Structured vs unstructured data.
- Common data sources: databases, spreadsheets, APIs, logs, surveys.

**Practice**
- Write one business problem and convert it into 5 measurable analytical questions.
- For each analytics type, give one retail example.

**Deliverable**
- One-page notes explaining the analytics lifecycle and your role as an analyst.

### Day 2 — Business Thinking, KPIs & Metrics
**Learn**
- KPI vs metric.
- Dimension vs measure.
- Leading vs lagging indicators.
- Revenue, units, average order value, conversion rate, margin, retention, growth rate.
- Business terminology: customer, order, product, region, segment, revenue, cost, profit.

**Practice**
Create a KPI dictionary with columns:
`KPI | Definition | Formula | Grain | Dimension(s) | Business use`.

**Deliverable**
- At least 10 KPIs and 10 business questions.

### Day 3 — Excel Fundamentals
**Learn**
- Tables, cell references, sorting, filtering, formatting.
- `SUM`, `SUMIF`, `SUMIFS`, `COUNTIF`, `COUNTIFS`, `AVERAGEIF`.
- `IF`, `IFERROR`, `AND`, `OR`.
- Text/date functions such as `LEFT`, `RIGHT`, `TRIM`, `TEXT`, `YEAR`, `MONTH`.
- Remove duplicates and identify blanks.

**Practice**
- Recreate common KPI calculations from the sample CSV after opening it in Excel.
- Add helper columns for `Revenue`, `Cost`, and `Profit`.

**Deliverable**
- A clean spreadsheet with formulas, filters, and a KPI summary.

### Day 4 — Excel Analysis & Visualisation
**Learn**
- Pivot tables and pivot charts.
- Conditional formatting.
- Grouping dates into months/quarters.
- Choosing column, bar, line, and scatter charts.
- Avoiding misleading scales and unnecessary decoration.

**Practice**
Build analyses for:
1. Sales by region.
2. Sales by category.
3. Monthly sales trend.
4. Profit by product.

**Deliverable**
- Dashboard wireframe plus 5 written insights.

### Day 5 — SQL Fundamentals
**Learn**
- `SELECT`, `WHERE`, `ORDER BY`, `LIMIT`.
- `DISTINCT`, aliases, arithmetic expressions.
- `GROUP BY`, `HAVING`.
- `CASE WHEN`.
- `INNER JOIN`, `LEFT JOIN`.
- NULL handling with `COALESCE`.

**Practice**
Complete every query in `sql/SQL_PRACTICE.sql` through section 1.

**Deliverable**
- 15 working SQL queries with a one-line explanation of each.

### Day 6 — Advanced SQL
**Learn**
- Subqueries.
- CTEs using `WITH`.
- Window functions: `ROW_NUMBER`, `RANK`, `DENSE_RANK`, `SUM() OVER`, `AVG() OVER`.
- Partitioning and ordering.
- Date aggregation and period comparisons.

**Practice**
Complete section 2 and explain the difference between `GROUP BY` and window functions.

**Deliverable**
- 10 advanced SQL queries and one top-N analysis.

### Day 7 — Python, Pandas & Statistics
**Learn**
- Python data structures and functions.
- Pandas `read_csv`, `head`, `info`, `describe`, `value_counts`.
- Selection with `loc`/`iloc`.
- `groupby`, `agg`, `merge`, `sort_values`.
- Mean, median, mode, range, variance, standard deviation.
- Percentiles and IQR.
- Correlation vs causation.

**Practice**
Run `python/eda_and_cleaning.py` and inspect every output.

**Deliverable**
- Data profile: shape, data types, missingness, duplicates, descriptive statistics, and initial hypotheses.

---

## Week 2 — Business Analytics, EDA, Power BI & Readiness

### Day 8 — Data Cleaning
**Learn**
- Data-quality dimensions: completeness, uniqueness, validity, consistency, accuracy.
- Missing-value strategies: investigate, remove, impute, or flag.
- Duplicate detection.
- Outlier detection using IQR and business rules.
- Standardising categories and dates.
- Avoiding leakage and accidental data loss.

**Practice**
- Detect the intentionally introduced missing discounts and duplicate transaction IDs in the sample dataset.
- Decide how each issue should be handled and document why.

**Deliverable**
- Cleaning log: `issue | detection rule | action | reason | impact`.

### Day 9 — Exploratory Data Analysis
**Learn**
- Univariate, bivariate, and multivariate analysis.
- Distributions, trends, correlations, segments, patterns, and anomalies.
- Comparing average vs median where skew is present.
- Drill-down from overall KPI to region/category/product.

**Practice**
Answer:
- What happened?
- What changed?
- Which segment performed best/worst?
- Why might the change have happened?
- What deserves further investigation?

**Deliverable**
- At least 8 evidence-backed insights with supporting figures or grouped tables.

### Day 10 — Power BI Data Model & Dashboard Design
**Learn**
- Importing data.
- Power Query for profiling and cleaning.
- Fact vs dimension tables.
- Relationships and star schema basics.
- Filter context and slicers.
- Dashboard layout and visual selection.

**Practice**
Design a one-page executive dashboard with:
- KPI cards: Gross Sales, Net Sales, Profit, Margin %.
- Monthly Net Sales line chart.
- Region bar chart.
- Category bar chart.
- Product/segment detail table.
- Slicers for date, region, category, and segment.

**Deliverable**
- Dashboard wireframe and model diagram.

### Day 11 — DAX
**Learn**
- Measures vs calculated columns.
- `SUM`, `COUNTROWS`, `DISTINCTCOUNT`, `DIVIDE`.
- `CALCULATE` and filter context.
- Time-intelligence concepts.
- `VAR` for readable measures.

**Practice**
Implement the measures in `powerbi/DAX_AND_DASHBOARD.md`.

**Deliverable**
- At least 8 reusable measures.

### Day 12 — Visualisation & Data Storytelling
**Learn**
- Start with the business question, not the chart.
- Context → evidence → insight → implication → action.
- Annotation and selective highlighting.
- Difference between observation and explanation.
- How to communicate uncertainty and limitations.

**Practice**
Create a 5-slide story:
1. Business objective.
2. Executive KPI snapshot.
3. Main trend and what changed.
4. Segment/product driver analysis.
5. Recommendations and next steps.

**Deliverable**
- Five-slide narrative plus a 60-second verbal explanation.

### Day 13 — End-to-End Mock Project
**Business brief**
You are a junior Data Analyst supporting a retail manager. Management wants to understand sales performance and identify the most actionable improvement opportunities.

**Workflow**
1. Inspect the raw dataset.
2. Define metrics and business questions.
3. Clean the data.
4. Validate assumptions.
5. Analyze with SQL and/or Python.
6. Build the Power BI design.
7. Write findings and recommendations.

**Minimum output**
- Cleaned-data description.
- KPI table.
- 8+ insights.
- 3+ recommendations.
- Limitations / assumptions.

**Deliverable**
- A concise analyst report suitable for a project manager.

### Day 14 — Prerequisite Assessment & Readiness Review
Use `assessment/PREREQUISITE_ASSESSMENT.md` as a timed mock test.

Suggested 120-minute split:
- Excel: 20 min
- SQL: 30 min
- Python/Pandas: 20 min
- Statistics & data cleaning: 15 min
- Power BI/DAX: 15 min
- Business case + interpretation: 20 min

**Readiness standard**
A project-ready analyst should be able to solve unfamiliar questions, explain assumptions, validate results, and communicate recommendations without depending on memorised answers.
