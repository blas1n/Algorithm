SELECT p.product_id, IFNULL((
    SELECT new_price FROM Products
    WHERE p.product_id = product_id and change_date <= '2019-08-16'
    ORDER BY change_date DESC LIMIT 1
), 10) as price FROM (SELECT DISTINCT product_id FROM Products) p