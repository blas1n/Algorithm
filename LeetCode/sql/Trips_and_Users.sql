SELECT
    t.request_at as Day,
    ROUND(SUM(IF(t.status <> 'completed', 1, 0)) / COUNT(*), 2) as 'Cancellation Rate'
FROM Trips t
LEFT JOIN Users c ON t.client_id = c.users_id
LEFT JOIN Users d ON t.driver_id = d.users_id
WHERE c.banned = 'No' AND d.banned = 'No' AND t.request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY request_at