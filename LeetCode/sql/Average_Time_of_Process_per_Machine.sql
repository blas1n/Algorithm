SELECT start.machine_id, ROUND(AVG(end.timestamp - start.timestamp), 3) as processing_time
    FROM Activity start
    LEFT JOIN Activity end ON start.machine_id = end.machine_id and start.process_id = end.process_id and end.activity_type = 'end'
    WHERE start.activity_type = 'start'
    GROUP BY start.machine_id