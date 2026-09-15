# Completed Mock Project — Retail Sales Analysis

**Analyst:** Ashutosh Yadav  
**Dataset:** Synthetic retail sales dataset  
**Period:** January–April 2026  

## 1. Business objective

Help the retail manager understand sales and profitability performance across time, regions, segments, categories, and products, then identify practical opportunities for improvement.

## 2. Data-quality findings

| Check | Result | Treatment |
|---|---:|---|
| Raw rows | 41 | Retained raw file unchanged |
| Unique transaction IDs after deduplication | 40 | Removed one duplicate T020 |
| Missing discounts | 1 | Filled with 0 for this training dataset; document treatment |
| Invalid units | 0 | No action required |
| Invalid discount range | 0 | No action required |
| Returned orders | 3 / 40 = 7.5% | Excluded from Net Sales and Profit |

**Important:** The duplicate transaction is intentionally present to test grain awareness. The raw dataset should be preserved; cleaning should happen in a derived dataset.

## 3. Executive KPIs

| KPI | Result |
|---|---:|
| Gross Sales | ₹480,370 |
| Net Sales | ₹450,930 |
| Cost | ₹312,040 |
| Profit | ₹138,890 |
| Profit Margin | 30.80% |
| Return Rate | 7.50% |

## 4. What happened?

Net Sales reached **₹450,930** for the four-month period, producing **₹138,890** profit and a **30.80%** overall margin.

Electronics is the main revenue category at **₹268,390** in Net Sales, followed by Furniture at **₹157,130**.

Corporate customers generated **₹287,880**, making the Corporate segment the largest contributor among the three segments.

## 5. What changed over time?

| Month | Net Sales | Month-over-month change |
|---|---:|---:|
| Jan 2026 | ₹70,840 | — |
| Feb 2026 | ₹117,500 | +65.87% |
| Mar 2026 | ₹140,800 | +19.83% |
| Apr 2026 | ₹121,790 | -13.50% |

The largest improvement occurred in February. March was the peak sales month. April then declined by about **13.5%** versus March, which is the most important trend to investigate next.

## 6. Regional performance

| Region | Net Sales | Share of Net Sales |
|---|---:|---:|
| North | ₹141,750 | 31.44% |
| South | ₹119,640 | 26.53% |
| East | ₹110,830 | 24.58% |
| West | ₹78,710 | 17.46% |

North is the leading region, while West is the weakest by Net Sales. This does not by itself prove West is underperforming on profitability, so margin and return behaviour should be checked before taking action.

## 7. Segment performance

| Segment | Net Sales |
|---|---:|
| Corporate | ₹287,880 |
| Consumer | ₹82,490 |
| Small Business | ₹80,560 |

Corporate contributes the majority of Net Sales. This suggests account-level analysis, repeat purchasing, and contract/discount behaviour could be useful follow-up analyses.

## 8. Product profitability

| Product | Net Sales | Profit | Margin % |
|---|---:|---:|---:|
| Monitor | ₹120,240 | ₹26,740 | 22.24% |
| Desk | ₹31,680 | ₹7,280 | 22.98% |
| Office Chair | ₹71,110 | ₹20,710 | 29.12% |
| Webcam | ₹43,520 | ₹13,120 | 30.15% |
| Bookshelf | ₹54,340 | ₹18,040 | 33.20% |
| Wireless Mouse | ₹25,400 | ₹8,900 | 35.04% |
| Keyboard | ₹26,220 | ₹10,120 | 38.60% |
| Headset | ₹53,010 | ₹22,010 | 41.52% |
| Planner | ₹17,010 | ₹7,770 | 45.68% |
| Notebook | ₹8,400 | ₹4,200 | 50.00% |

Monitor is the largest product by Net Sales but has a relatively low margin of **22.24%**. This is a classic case where revenue leadership does not automatically mean the best profitability.

## 9. Business recommendations

### Recommendation 1 — Investigate the April decline
Compare April vs March by region, segment, and product to find the specific drivers of the **13.5%** decline before changing pricing or marketing.

### Recommendation 2 — Review Monitor and Desk economics
These products have the lowest product-level margins in the dataset. Review pricing, unit cost, discounting, supplier terms, and return behaviour before increasing promotion.

### Recommendation 3 — Protect high-value Corporate demand
Corporate customers account for most Net Sales. Analyze repeat orders, account concentration, discounts, and churn/retention indicators to understand whether this revenue is durable.

### Recommendation 4 — Investigate return drivers
A 7.5% return rate is material enough to monitor. Break returns down by region, product, and segment and distinguish operational issues from normal return behaviour.

## 10. Limitations

- The dataset is synthetic and very small.
- It covers only four months, so seasonal effects cannot be established.
- There is no customer ID, order channel, supplier information, geography below region, or marketing data.
- Causal explanations cannot be proven from this dataset alone; they require additional evidence.

## 11. Project-ready analyst takeaway

The correct workflow is not simply to calculate a total. A project-ready analyst should validate data quality, define metric logic, compare performance across meaningful dimensions, identify changes and likely drivers, communicate uncertainty, and turn evidence into actionable recommendations.
