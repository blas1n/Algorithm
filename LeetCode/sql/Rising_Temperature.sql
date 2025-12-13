SELECT today.id FROM Weather today
    LEFT JOIN Weather yesterday ON yesterday.recordDate = DATE_SUB(today.recordDate, INTERVAL 1 DAY)
    WHERE yesterday.temperature < today.temperature