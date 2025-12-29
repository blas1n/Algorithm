WITH t as (
    SELECT requester_id as id FROM RequestAccepted
    UNION ALL
    SELECT accepter_id as id FROM RequestAccepted
)
SELECT id, COUNT(id) as num
FROM t
GROUP BY id
ORDER BY COUNT(id) DESC LIMIT 1