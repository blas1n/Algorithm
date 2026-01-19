SELECT t.employee_id
FROM (
    SELECT * FROM Employees LEFT JOIN Salaries USING(employee_id)
    UNION 
    SELECT * FROM Employees RIGHT JOIN Salaries USING(employee_id)
) AS t
WHERE t.salary IS NULL OR t.name IS NULL
ORDER BY employee_id;