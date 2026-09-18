# Final Data Analyst Prerequisite — Presentation

**Candidate:** Ashutosh Yadav  
**Repository:** `Ashutosh-76-pro/data-science-internship`

---

## Slide 1 — Title

**Data Analyst 14-Day Prerequisite & Project Readiness**

Excel | SQL | Advanced SQL | Python | Pandas | Statistics | EDA | Power BI | DAX

**Candidate:** Ashutosh Yadav

---

## Slide 2 — Objective

### Goal

Build the technical, analytical, business and communication capability required to work independently on an industry-oriented Data Analyst project.

### Learning flow

**Self-Learning → Practice → Assessment → Project Readiness → Industry-Ongoing Project**

---

## Slide 3 — 14-Day Roadmap

### Week 1
- Analytics fundamentals
- Business thinking and KPIs
- Excel
- SQL and Advanced SQL
- Python/Pandas
- Statistics

### Week 2
- Data cleaning
- EDA
- Power BI
- DAX
- Visualization and storytelling
- Mock project
- Prerequisite assessment

---

## Slide 4 — End-to-End Analytics Workflow

**Business question**  
↓  
**Understand dataset and grain**  
↓  
**Profile & validate data**  
↓  
**Clean & transform**  
↓  
**Calculate KPIs**  
↓  
**Analyze with SQL/Python**  
↓  
**Visualize in Power BI**  
↓  
**Generate evidence-backed insights**  
↓  
**Recommend next actions**

---

## Slide 5 — Dataset Used

**Synthetic Retail Sales Dataset**

Fields include:

- Transaction ID
- Order date
- Region
- Customer segment
- Product category
- Product
- Units
- Unit price
- Unit cost
- Discount
- Return status

The same dataset supports the Excel, SQL, Python, EDA and Power BI learning workflow.

---

## Slide 6 — Data Quality

### Issues intentionally present for practice

- **41 raw rows**
- **1 duplicate transaction ID:** T020
- **1 missing discount value**
- Text/date/numeric standardisation required
- Returned orders require explicit metric logic

### Treatment

Duplicate transaction IDs are removed at the transaction grain. The missing discount is filled with 0 for this training scenario and the treatment is documented.

---

## Slide 7 — KPI Framework

### Core KPIs

- Gross Sales
- Net Sales
- Cost
- Profit
- Profit Margin %
- Return Rate
- Sales by Region
- Sales by Category
- Monthly Net Sales

### Example formula

**Profit Margin % = Profit ÷ Net Sales × 100**

---

## Slide 8 — Executive KPI Snapshot

From the cleaned training analysis:

| KPI | Result |
|---|---:|
| Gross Sales | ₹480,370 |
| Net Sales | ₹450,930 |
| Cost | ₹312,040 |
| Profit | ₹138,890 |
| Profit Margin | 30.80% |
| Return Rate | 7.50% |

---

## Slide 9 — Trend Analysis

### Monthly Net Sales

| Month | Net Sales | MoM Change |
|---|---:|---:|
| Jan 2026 | ₹70,840 | — |
| Feb 2026 | ₹117,500 | +65.87% |
| Mar 2026 | ₹140,800 | +19.83% |
| Apr 2026 | ₹121,790 | -13.50% |

### Key observation

March is the peak month. April's decline should be investigated by region, segment and product before a business action is taken.

---

## Slide 10 — Segment & Regional Analysis

### Segment

- Corporate: **₹287,880**
- Consumer: **₹82,490**
- Small Business: **₹80,560**

### Region

- North: **₹141,750**
- South: **₹119,640**
- East: **₹110,830**
- West: **₹78,710**

Revenue leadership should be separated from profitability and return behaviour before drawing conclusions.

---

## Slide 11 — Product Profitability

Selected product-level margin results:

| Product | Net Sales | Margin |
|---|---:|---:|
| Monitor | ₹120,240 | 22.24% |
| Office Chair | ₹71,110 | 29.12% |
| Bookshelf | ₹54,340 | 33.20% |
| Headset | ₹53,010 | 41.52% |
| Planner | ₹17,010 | 45.68% |
| Notebook | ₹8,400 | 50.00% |

### Insight

Monitor has the largest Net Sales among the listed products but a comparatively low margin, showing why revenue alone is not enough for product decisions.

---

## Slide 12 — Python / Pandas

### Practical workflow

- Load CSV with Pandas
- Profile shape and data types
- Inspect missing values
- Remove duplicate transaction IDs
- Standardise text fields
- Create Gross Sales, Net Sales, Cost and Profit
- Group by month, region and category
- Detect possible IQR outliers
- Generate charts

**Source:** `data-analyst-prerequisite/python/eda_and_cleaning.py`

---

## Slide 13 — SQL & Advanced SQL

### Fundamental SQL

- SELECT / WHERE
- ORDER BY / LIMIT
- GROUP BY / HAVING
- CASE
- COALESCE

### Advanced SQL

- CTEs
- LAG
- DENSE_RANK
- Window aggregates
- Contribution/share analysis
- Data-quality queries

**Source:** `data-analyst-prerequisite/sql/SQL_PRACTICE.sql`

---

## Slide 14 — Power BI & DAX

### Dashboard design

- KPI cards
- Monthly trend
- Regional comparison
- Category comparison
- Product detail
- Return-rate analysis
- Date/region/category slicers

### DAX concepts

- Measures vs calculated columns
- SUM
- COUNTROWS
- DISTINCTCOUNT
- DIVIDE
- CALCULATE
- Filter context
- VAR

---

## Slide 15 — Business Storytelling

### Insight structure

**Observation → Evidence → Implication → Action**

Example:

**Observation:** April Net Sales declined.  
**Evidence:** ₹121,790 vs ₹140,800 in March, a 13.5% decline.  
**Implication:** The source of the decline should be isolated before changing pricing or promotion.  
**Action:** Compare April vs March by region, segment and product.

---

## Slide 16 — Recommendations

1. Investigate the April decline at region, segment and product level.
2. Review Monitor and other lower-margin products for pricing, cost, discount and return behaviour.
3. Protect Corporate demand by examining repeat orders, account concentration and discount patterns.
4. Break the 7.5% return rate down by product, region and segment.

Recommendations should be connected to evidence and should not be presented as proven causal conclusions when the dataset cannot establish causation.

---

## Slide 17 — Assessment Readiness

The mock assessment covers:

- Excel
- SQL
- Advanced SQL
- Data cleaning
- Statistics
- Python/Pandas
- EDA
- Power BI
- DAX
- Visualization
- KPIs
- Business analytics
- Interpretation
- Case studies
- Practical tasks

Recommended mock-test duration: **120 minutes**

---

## Slide 18 — Repository Structure

```text
data-science-internship/
├── data-analyst-prerequisite/
├── Datasets/
├── Source Codes/
├── Documentation/
└── PPT / Slides/
```

### Documentation

Reports, learning log, data dictionary and assessment readiness.

### PPT / Slides

This final presentation plus the original prerequisite summary deck.

---

## Slide 19 — Project Readiness

### Evidence of preparation

- Technical practice files
- Synthetic dataset
- Python EDA workflow
- SQL practice
- Power BI/DAX guidance
- End-to-end capstone analysis
- Mock prerequisite assessment
- Documentation and presentation

**Project assignment should depend on actual assessment performance and the required organisational standard.**

---

## Slide 20 — Closing

### Key takeaway

A Data Analyst is expected to do more than calculate totals.

The target capability is to:

**Understand the question → validate the data → analyze correctly → explain the evidence → communicate clearly → recommend next actions**

**Thank you**

