# Power BI DAX Measures

Assume a model table named `Sales`.

```DAX
Total Sales = SUMX(Sales, Sales[Units] * Sales[Unit Price] * (1 - COALESCE(Sales[Discount], 0)))

Net Sales =
SUMX(
    Sales,
    IF(
        Sales[Returned] = "Yes",
        0,
        Sales[Units] * Sales[Unit Price] * (1 - COALESCE(Sales[Discount], 0))
    )
)

Total Cost =
SUMX(
    Sales,
    IF(Sales[Returned] = "Yes", 0, Sales[Units] * Sales[Unit Cost])
)

Total Profit = [Net Sales] - [Total Cost]

Profit Margin % = DIVIDE([Total Profit], [Net Sales], 0)

Return Rate % = DIVIDE(CALCULATE(COUNTROWS(Sales), Sales[Returned] = "Yes"), COUNTROWS(Sales), 0)
```

Format `Profit Margin %` and `Return Rate %` as percentages.
