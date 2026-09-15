# Excel Practice — Data Analyst Prerequisite

Use the CSV in `../data/sales_data.csv`. Open it in Excel and convert the range into an Excel Table named `Sales`.

## 1. Add calculated columns

Create these columns using formulas:

**Gross Sales**
```excel
=[@units]*[@unit_price]*(1-IFERROR([@discount],0))
```

**Net Sales**
```excel
=IF([@returned]="Yes",0,[@[Gross Sales]])
```

**Cost**
```excel
=IF([@returned]="Yes",0,[@units]*[@unit_cost])
```

**Profit**
```excel
=[@[Net Sales]]-[@Cost]
```

**Margin %**
```excel
=IFERROR([@Profit]/[@[Net Sales]],0)
```

## 2. Data-quality checks

Answer these before changing the data:

1. How many missing discounts are present?
2. Which transaction ID appears more than once?
3. Are any units negative or zero?
4. Are any discount values outside 0–100%?
5. Are region/category/segment labels consistent?

Recommended approach: record every change in a cleaning log instead of silently overwriting raw data.

## 3. KPI calculations

Create a small KPI panel for:

| KPI | Formula idea |
|---|---|
| Gross Sales | `SUM(Sales[Gross Sales])` |
| Net Sales | `SUM(Sales[Net Sales])` |
| Profit | `SUM(Sales[Profit])` |
| Margin % | `Profit / Net Sales` |
| Orders | `COUNTA(Sales[transaction_id])` after deduplication |
| Returned Orders | `COUNTIF(Sales[returned],"Yes")` |
| Return Rate | `Returned Orders / Orders` |
| Units Sold | `SUM(Sales[units])` |

## 4. Practice questions

### Basic
1. Find net sales for the North region.
2. Count Corporate orders.
3. Find the average unit price for Electronics.
4. Find the highest-profit product.
5. Calculate sales from orders with a discount of at least 10%.

### Analytical
6. Which region has the highest net sales?
7. Which category has the highest profit?
8. Which product has the lowest margin %?
9. Compare returned vs non-returned gross sales.
10. Calculate each region's share of total net sales.

### Pivot table practice
Build these PivotTables:

- Rows = Region; Values = Sum of Net Sales and Sum of Profit.
- Rows = Category; Values = Sum of Net Sales and Average of Margin %.
- Rows = Product; Columns = Segment; Values = Sum of Net Sales.
- Rows = Order Date grouped by Month; Values = Sum of Net Sales.

## 5. Chart selection

Use a line chart for monthly trend, a bar/column chart for region or category comparison, and a scatter plot for a relationship such as units vs net sales.

Write one sentence below every chart answering the business question it was created to answer.

## 6. Excel readiness checklist

- [ ] I can use relative and absolute references.
- [ ] I can use `SUMIFS` and `COUNTIFS`.
- [ ] I can clean duplicates and blanks.
- [ ] I can build a PivotTable.
- [ ] I can select an appropriate chart.
- [ ] I can explain a result in business language rather than only reporting a number.
