SELECT
    transaction_date,
    SUM(IF(amount % 2 = 0, 0, amount)) as odd_sum,
    SUM(IF(amount % 2 = 0, amount, 0)) as even_sum
FROM Transactions
GROUP BY transaction_date
ORDER BY transaction_date