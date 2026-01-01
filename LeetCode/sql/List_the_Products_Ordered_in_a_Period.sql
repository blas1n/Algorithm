SELECT p.product_name, SUM(unit) as unit
FROM Orders o
RIGHT JOIN Products p ON p.product_id = o.product_id
WHERE YEAR(o.order_date) = 2020 and MONTH(o.order_date) = 2
GROUP BY p.product_name HAVING SUM(o.unit) >= 100