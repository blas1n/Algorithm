# Write your MySQL query statement below
WITH CTE1 AS (
    SELECT 
        s.product_id,
        s.quantity,
        s.price,
        p.category,
        CASE 
            WHEN MONTH(sale_date) IN (12, 1, 2) THEN 'Winter'
            WHEN MONTH(sale_date) IN (3, 4, 5)  THEN 'Spring'
            WHEN MONTH(sale_date) IN (6, 7, 8)  THEN 'Summer'
            ELSE 'Fall'
        END AS season
    FROM Sales s
    JOIN Products p ON s.product_id = p.product_id
),
CTE2 AS (
    SELECT 
        season,
        category,
        SUM(quantity) as total_quantity,
        SUM(quantity * price) as total_revenue,
        RANK() OVER (
            PARTITION BY season
            ORDER BY
                SUM(quantity) DESC,
                SUM(quantity * price) DESC,
                category ASC
        ) AS rnk
    FROM CTE1
    GROUP BY season, category
)
SELECT 
    season,
    category,
    total_quantity,
    total_revenue
FROM CTE2
WHERE rnk = 1
ORDER BY season;