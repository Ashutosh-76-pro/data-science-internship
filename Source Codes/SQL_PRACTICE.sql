-- Data Analyst Prerequisite SQL Practice
-- PostgreSQL-compatible syntax. Load Datasets/sales_data.csv into table sales.

SELECT * FROM sales LIMIT 10;
SELECT DISTINCT region FROM sales ORDER BY region;
SELECT transaction_id, product, units FROM sales WHERE units > 5 ORDER BY units DESC;

SELECT region, SUM(units * unit_price * (1 - COALESCE(discount,0))) AS gross_sales
FROM sales GROUP BY region ORDER BY gross_sales DESC;

SELECT category,
SUM(CASE WHEN returned='Yes' THEN 0 ELSE units * unit_price * (1-COALESCE(discount,0)) END) AS net_sales
FROM sales GROUP BY category ORDER BY net_sales DESC;

SELECT region, COUNT(*) AS orders,
SUM(CASE WHEN returned='Yes' THEN 1 ELSE 0 END) AS returned_orders,
100.0*SUM(CASE WHEN returned='Yes' THEN 1 ELSE 0 END)/COUNT(*) AS return_rate_pct
FROM sales GROUP BY region ORDER BY return_rate_pct DESC;

SELECT transaction_id, COUNT(*) AS occurrences
FROM sales GROUP BY transaction_id HAVING COUNT(*) > 1;

WITH monthly AS (
 SELECT DATE_TRUNC('month',order_date)::date AS month,
 SUM(CASE WHEN returned='Yes' THEN 0 ELSE units*unit_price*(1-COALESCE(discount,0)) END) AS net_sales
 FROM sales GROUP BY 1
)
SELECT month, net_sales,
LAG(net_sales) OVER (ORDER BY month) AS previous_month,
100.0*(net_sales-LAG(net_sales) OVER (ORDER BY month))/NULLIF(LAG(net_sales) OVER (ORDER BY month),0) AS growth_pct
FROM monthly ORDER BY month;

WITH product_sales AS (
 SELECT category, product,
 SUM(CASE WHEN returned='Yes' THEN 0 ELSE units*unit_price*(1-COALESCE(discount,0)) END) AS net_sales
 FROM sales GROUP BY category, product
)
SELECT category, product, net_sales,
DENSE_RANK() OVER (PARTITION BY category ORDER BY net_sales DESC) AS category_rank
FROM product_sales ORDER BY category, category_rank;

WITH region_sales AS (
 SELECT region,
 SUM(CASE WHEN returned='Yes' THEN 0 ELSE units*unit_price*(1-COALESCE(discount,0)) END) AS net_sales
 FROM sales GROUP BY region
)
SELECT region, net_sales, 100.0*net_sales/SUM(net_sales) OVER () AS sales_share_pct
FROM region_sales ORDER BY net_sales DESC;

SELECT COUNT(*) AS rows,
COUNT(*)-COUNT(discount) AS missing_discounts,
SUM(CASE WHEN returned NOT IN ('Yes','No') OR returned IS NULL THEN 1 ELSE 0 END) AS invalid_return_flags
FROM sales;
