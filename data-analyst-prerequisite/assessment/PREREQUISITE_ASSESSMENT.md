# Data Analyst Prerequisite Assessment — Mock Test

**Candidate:** Ashutosh Yadav  
**Recommended time:** 120 minutes  
**Rule:** Solve independently. Show assumptions and reasoning.

This is a practice assessment aligned with the 2-week prerequisite. It tests application rather than memorised definitions.

## Section A — Excel (15 marks)

Use `data/sales_data.csv` in Excel.

1. Identify the missing discount value(s) and explain your treatment. (2)
2. Identify duplicate transaction ID(s) and explain which record should remain. (2)
3. Calculate Gross Sales, Net Sales, Cost, Profit, and Margin %. (4)
4. Use a PivotTable to find Net Sales by Region. (2)
5. Use a PivotTable to find Profit by Category. (2)
6. Create a monthly Net Sales chart and write two evidence-based insights. (3)

## Section B — SQL (25 marks)

Assume the data is loaded into a table named `sales`.

1. Return all distinct regions in alphabetical order. (2)
2. Find the total Net Sales by region, excluding returned orders. (3)
3. Return the top 3 products by Net Sales. (3)
4. Calculate return rate by region. (3)
5. Find duplicate transaction IDs. (2)
6. Calculate profit by product. (3)
7. Use a CTE to calculate monthly Net Sales. (3)
8. Use a window function to rank products within each category. (3)
9. Explain when `HAVING` is used instead of `WHERE`. (3)

## Section C — Python / Pandas (20 marks)

1. Load the CSV using Pandas and display shape, data types, and missing values. (3)
2. Remove duplicate transaction IDs and document the impact on row count. (3)
3. Treat missing discounts and explain why your chosen treatment is reasonable. (3)
4. Create `gross_sales`, `net_sales`, `cost`, and `profit`. (4)
5. Produce Net Sales by region and category. (3)
6. Detect possible outliers using IQR and distinguish statistical outliers from legitimate business observations. (2)
7. State two limitations of the analysis. (2)

## Section D — Statistics & Data Cleaning (15 marks)

1. Explain mean vs median and when median may be preferable. (3)
2. Explain standard deviation in business terms. (2)
3. Explain the difference between correlation and causation. (3)
4. Name four dimensions of data quality. (2)
5. Give one appropriate strategy for handling missing values and one situation where dropping rows can be dangerous. (3)
6. Explain why duplicates must be considered at the correct data grain. (2)

## Section E — Power BI & DAX (10 marks)

1. Explain a measure vs a calculated column. (2)
2. Write a DAX measure for Margin %. (2)
3. Write a DAX measure for Return Rate %. (2)
4. Name five visuals or dashboard components you would use for this business case and explain why. (2)
5. Explain filter context in practical terms. (2)

## Section F — Business Case & Storytelling (15 marks)

You are presenting to a retail manager.

1. State the business objective in one sentence. (2)
2. Identify the most useful three KPIs for the manager and justify each. (3)
3. Write three findings using the structure **observation → evidence → implication**. (5)
4. Give three recommendations that are actionable, specific, and connected to the findings. (3)
5. State two analyses you would perform next if more data became available. (2)

## Suggested scoring rubric

| Score | Readiness interpretation |
|---|---|
| 90–100 | Strong project-ready performance |
| 75–89 | Good readiness; close technical gaps |
| 60–74 | Needs targeted practice before project assignment |
| Below 60 | Revisit fundamentals and repeat the assessment |

### Critical fail areas

A strong total score should not hide major weaknesses. Rework the assessment before claiming project readiness if you cannot independently:

- Clean a small dataset safely.
- Write basic SQL aggregation and joins.
- Use Pandas for profiling and grouped analysis.
- Calculate KPIs correctly.
- Explain findings in business language.

## Final reflection

After finishing, write 5–10 lines answering:

1. Which section was hardest?
2. Which mistakes did you make?
3. Which skills can you now perform without guidance?
4. What will you practice during the next 7 days?
5. What would you verify before presenting a KPI to a manager?
