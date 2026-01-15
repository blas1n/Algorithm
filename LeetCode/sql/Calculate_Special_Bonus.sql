SELECT
    employee_id,
    IF(employee_id % 2 > 0 and LEFT(name, 1) <> 'M', salary, 0) as bonus
FROM Employees
ORDER BY employee_id