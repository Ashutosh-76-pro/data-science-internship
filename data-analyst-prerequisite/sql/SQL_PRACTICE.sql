-- Data Analyst Prerequisite SQL Practice
-- Assumption: the CSV has been loaded into a table named sales.
-- PostgreSQL-compatible syntax is used where practical.

-- Suggested table schema:
-- sales(
--   transaction_id text, order_date date, region text, segment text,
--   category text, product text, units int, unit_price numeric,
--   unit_cost numeric, discount numeric, returned text
-- )

/* ================================================================
   SECTION 1 — SQL FUNDAMENTALS
   ================================================================ */

-- 1. Show the first 10 records.
SELECT *
FROM sales
LIMIT 10;

-- 2. List unique regions.
SELECT DISTINCT region
FROM sales
ORDER BY region;

-- 3. Find orders with more than 5 units.
SELECT transaction_id, product, units
FROM sales
WHERE units > 5
ORDER BY units DESC;

-- 4. Calculate discounted sales for every row.
SELECT
    transaction_id,
    units * unit_price * (1 - COALESCE(discount, 0)) AS gross_sales
FROM sales;

-- 5. Total sales by region.
SELECT
    region,
    SUM(units * unit_price * (1 - COALESCE(discount, 0))) AS gross_sales
FROM sales
GROUP BY region
ORDER BY gross_sales DESC;

-- 6. Net sales by category; returned orders contribute zero.
SELECT
    category,
    SUM(
        CASE WHEN returned = 'Yes' THEN 0
             ELSE units * unit_price * (1 - COALESCE(discount, 0))
        END
    ) AS net_sales
FROM sales
GROUP BY category
ORDER BY net_sales DESC;

-- 7. Count orders by customer segment.
SELECT segment, COUNT(*) AS order_count
FROM sales
GROUP BY segment
ORDER BY order_count DESC;

-- 8. Find categories with net sales above 10000.
SELECT
    category,
    SUM(
        CASE WHEN returned = 'Yes' THEN 0
             ELSE units * unit_price * (1 - COALESCE(discount, 0))
        END
    ) AS net_sales
FROM sales
GROUP BY category
HAVING SUM(
    CASE WHEN returned = 'Yes' THEN 0
         ELSE units * unit_price * (1 - COALESCE(discount, 0))
    END
) > 10000
ORDER BY net_sales DESC;

-- 9. Return count and return rate by region.
SELECT
    region,
    COUNT(*) AS orders,
    SUM(CASE WHEN returned = 'Yes' THEN 1 ELSE 0 END) AS returned_orders,
    100.0 * SUM(CASE WHEN returned = 'Yes' THEN 1 ELSE 0 END) / COUNT(*) AS return_rate_pct
FROM sales
GROUP BY region
ORDER BY return_rate_pct DESC;

-- 10. Identify duplicate transaction IDs.
SELECT transaction_id, COUNT(*) AS occurrences
FROM sales
GROUP BY transaction_id
HAVING COUNT(*) > 1;

-- 11. Replace missing discount with zero for analysis and calculate profit.
SELECT
    transaction_id,
    CASE WHEN returned = 'Yes' THEN 0
         ELSE units * unit_price * (1 - COALESCE(discount, 0))
    END AS net_sales,
    CASE WHEN returned = 'Yes' THEN 0
         ELSE units * unit_cost
    END AS cost,
    CASE WHEN returned = 'Yes' THEN 0
         ELSE units * unit_price * (1 - COALESCE(discount, 0)) - units * unit_cost
    END AS profit
FROM sales;

-- 12. Top 5 products by net sales.
SELECT
    product,
    SUM(
        CASE WHEN returned = 'Yes' THEN 0
             ELSE units * unit_price * (1 - COALESCE(discount, 0))
        END
    ) AS net_sales
FROM sales
GROUP BY product
ORDER BY net_sales DESC
LIMIT 5;

/* ================================================================
   SECTION 2 — ADVANCED SQL
   ================================================================ */

-- 13. CTE: monthly net sales.
WITH monthly AS (
    SELECT
        DATE_TRUNC('month', order_date)::date AS month,
        SUM(
            CASE WHEN returned = 'Yes' THEN 0
                 ELSE units * unit_price * (1 - COALESCE(discount, 0))
            END
        ) AS net_sales
    FROM sales
    GROUP BY 1
)
SELECT *
FROM monthly
ORDER BY month;

-- 14. Month-over-month change using LAG.
WITH monthly AS (
    SELECT
        DATE_TRUNC('month', order_date)::date AS month,
        SUM(
            CASE WHEN returned = 'Yes' THEN 0
                 ELSE units * unit_price * (1 - COALESCE(discount, 0))
            END
        ) AS net_sales
    FROM sales
    GROUP BY 1
)
SELECT
    month,
    net_sales,
    LAG(net_sales) OVER (ORDER BY month) AS previous_month_sales,
    net_sales - LAG(net_sales) OVER (ORDER BY month) AS absolute_change,
    100.0 * (net_sales - LAG(net_sales) OVER (ORDER BY month))
        / NULLIF(LAG(net_sales) OVER (ORDER BY month), 0) AS growth_pct
FROM monthly
ORDER BY month;

-- 15. Rank products within each category by net sales.
WITH product_sales AS (
    SELECT
        category,
        product,
        SUM(
            CASE WHEN returned = 'Yes' THEN 0
                 ELSE units * unit_price * (1 - COALESCE(discount, 0))
            END
        ) AS net_sales
    FROM sales
    GROUP BY category, product
)
SELECT
    category,
    product,
    net_sales,
    DENSE_RANK() OVER (PARTITION BY category ORDER BY net_sales DESC) AS category_rank
FROM product_sales
ORDER BY category, category_rank;

-- 16. Region contribution to overall net sales.
WITH region_sales AS (
    SELECT
        region,
        SUM(
            CASE WHEN returned = 'Yes' THEN 0
                 ELSE units * unit_price * (1 - COALESCE(discount, 0))
            END
        ) AS net_sales
    FROM sales
    GROUP BY region
)
SELECT
    region,
    net_sales,
    100.0 * net_sales / SUM(net_sales) OVER () AS sales_share_pct
FROM region_sales
ORDER BY net_sales DESC;

-- 17. Detect records with unusually high discounts.
SELECT *
FROM sales
WHERE COALESCE(discount, 0) >= 0.15
ORDER BY discount DESC;

-- 18. Business case: products with positive sales but below 20% margin.
WITH product_profit AS (
    SELECT
        product,
        SUM(CASE WHEN returned = 'Yes' THEN 0 ELSE units * unit_price * (1 - COALESCE(discount, 0)) END) AS net_sales,
        SUM(CASE WHEN returned = 'Yes' THEN 0 ELSE units * unit_cost END) AS cost
    FROM sales
    GROUP BY product
)
SELECT
    product,
    net_sales,
    cost,
    net_sales - cost AS profit,
    100.0 * (net_sales - cost) / NULLIF(net_sales, 0) AS margin_pct
FROM product_profit
WHERE net_sales > 0
  AND 100.0 * (net_sales - cost) / NULLIF(net_sales, 0) < 20
ORDER BY margin_pct;

-- 19. Find the top region/category combination.
SELECT
    region,
    category,
    SUM(CASE WHEN returned = 'Yes' THEN 0 ELSE units * unit_price * (1 - COALESCE(discount, 0)) END) AS net_sales
FROM sales
GROUP BY region, category
ORDER BY net_sales DESC
LIMIT 1;

-- 20. Data-quality summary.
SELECT
    COUNT(*) AS row_count,
    COUNT(*) - COUNT(discount) AS missing_discounts,
    SUM(CASE WHEN returned NOT IN ('Yes', 'No') OR returned IS NULL THEN 1 ELSE 0 END) AS invalid_return_flags,
    SUM(CASE WHEN units <= 0 OR unit_price < 0 OR unit_cost < 0 THEN 1 ELSE 0 END) AS invalid_numeric_rows
FROM sales;
