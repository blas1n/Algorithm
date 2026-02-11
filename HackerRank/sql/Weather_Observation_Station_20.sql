WITH CTE AS (
    SELECT LAT_N,
           ROW_NUMBER() OVER (ORDER BY LAT_N ASC) AS rn,
           COUNT(*) OVER () AS total_count
    FROM Station
)
SELECT ROUND(AVG(LAT_N), 4) AS median
FROM CTE
WHERE rn BETWEEN total_count / 2.0 AND total_count / 2.0 + 1;