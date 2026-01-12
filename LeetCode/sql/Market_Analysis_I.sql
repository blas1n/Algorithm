SELECT
    user_id as buyer_id,
    join_date,
    SUM(IF(YEAR(order_date) = 2019, 1, 0)) as orders_in_2019
FROM Users u
LEFT JOIN Orders o ON u.user_id = o.buyer_id
GROUP BY user_id