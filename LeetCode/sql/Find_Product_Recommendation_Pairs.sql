WITH CTE AS (
    SELECT pp.user_id, pp.product_id, pi.category FROM ProductPurchases pp
    JOIN ProductInfo pi ON pp.product_id = pi.product_id
)
SELECT
    p1.product_id as product1_id,
    p2.product_id as product2_id,
    p1.category as product1_category,
    p2.category as product2_category,
    COUNT(*) as customer_count
FROM CTE p1
JOIN CTE p2 ON p1.user_id = p2.user_id AND p1.product_id < p2.product_id
GROUP BY p1.product_id, p2.product_id
HAVING COUNT(*) >= 3
ORDER BY COUNT(*) DESC, p1.product_id, p2.product_id