WITH s AS (
    SELECT IF(
        id % 2 = 0,
        id - 1,
        IF(
            id = (SELECT MAX(id) FROM Seat),
            id,
            id + 1
        )) as swap_id,
        student
    FROM Seat
)
SELECT swap_id as id, student FROM s
ORDER BY swap_id
