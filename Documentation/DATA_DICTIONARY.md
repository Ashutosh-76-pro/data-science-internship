# Data Dictionary

| Field | Type | Meaning |
|---|---|---|
| transaction_id | Text | Unique transaction identifier |
| order_date | Date | Date of order |
| region | Text | Sales region |
| segment | Text | Customer/business segment |
| category | Text | Product category |
| product | Text | Product name |
| units | Integer | Quantity sold |
| unit_price | Numeric | Selling price per unit (₹) |
| unit_cost | Numeric | Cost per unit (₹) |
| discount | Decimal | Discount fraction, e.g. 0.10 = 10% |
| returned | Text | Whether the order was returned |

## Derived metrics
- Gross Sales = Units × Unit Price × (1 − Discount)
- Net Sales = Gross Sales for non-returned orders; 0 for returned orders
- Cost = Units × Unit Cost for non-returned orders
- Profit = Net Sales − Cost
- Profit Margin % = Profit ÷ Net Sales × 100
- Return Rate % = Returned Orders ÷ Total Orders × 100
