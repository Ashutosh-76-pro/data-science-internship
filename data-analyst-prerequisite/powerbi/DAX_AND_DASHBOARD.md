# Power BI & DAX Practice

## Recommended model

For this small exercise, a single cleaned fact-like table is acceptable. In a larger project, prefer a star schema with a sales fact table and dimensions such as Date, Product, Customer, and Region.

### Core fields
`transaction_id, order_date, region, segment, category, product, units, unit_price, unit_cost, discount, returned`

Create derived logic with Power Query or DAX rather than hardcoding results into visuals.

## Core DAX measures

Assume the table is named `Sales`.

### Gross Sales
```DAX
Gross Sales =
SUMX(
    Sales,
    Sales[units] * Sales[unit_price] * (1 - COALESCE(Sales[discount], 0))
)
```

### Net Sales
```DAX
Net Sales =
SUMX(
    Sales,
    IF(
        Sales[returned] = "Yes",
        0,
        Sales[units] * Sales[unit_price] * (1 - COALESCE(Sales[discount], 0))
    )
)
```

### Cost
```DAX
Cost =
SUMX(
    Sales,
    IF(Sales[returned] = "Yes", 0, Sales[units] * Sales[unit_cost])
)
```

### Profit
```DAX
Profit = [Net Sales] - [Cost]
```

### Margin %
```DAX
Margin % = DIVIDE([Profit], [Net Sales], 0)
```

### Order Count
```DAX
Order Count = DISTINCTCOUNT(Sales[transaction_id])
```

### Returned Orders
```DAX
Returned Orders =
CALCULATE(
    [Order Count],
    Sales[returned] = "Yes"
)
```

### Return Rate %
```DAX
Return Rate % = DIVIDE([Returned Orders], [Order Count], 0)
```

### Average Order Value
```DAX
Average Order Value = DIVIDE([Net Sales], [Order Count], 0)
```

## Dashboard design

Create a one-page executive dashboard with this hierarchy:

1. **Top row — KPI cards:** Net Sales, Profit, Margin %, Return Rate %.
2. **Middle left:** Monthly Net Sales line chart.
3. **Middle right:** Net Sales by Region horizontal bar chart.
4. **Bottom left:** Net Sales and Profit by Category.
5. **Bottom right:** Product performance table with Product, Net Sales, Profit, Margin %.
6. **Slicers:** Date, Region, Segment, Category.

## Storytelling rules

Every visual should answer a question. Example narrative:

> Net sales increased across the observed period, but performance differs by region and category. Management should focus on the strongest revenue drivers while investigating low-margin products and returned orders before scaling discounts.

Replace this example with your own evidence after running the analysis.

## DAX practice questions

1. Create a measure for units sold excluding returned orders.
2. Create a measure for average discount.
3. Rank products by Net Sales.
4. Calculate region contribution to total Net Sales.
5. Create a measure that compares current month sales with the previous month.
6. Explain why a measure is usually preferable to manually entering a total into a report.

## Readiness checklist

- [ ] I understand filter context at a practical level.
- [ ] I can distinguish measures from calculated columns.
- [ ] I can use `CALCULATE` and `DIVIDE`.
- [ ] I can build KPI cards and slicers.
- [ ] I can explain why a visual supports a business question.
- [ ] I can identify a misleading chart and improve it.
