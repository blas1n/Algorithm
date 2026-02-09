SELECT
    MAX(Salary * Months),
    COUNT(*)
FROM Employee
WHERE Salary * Months in (
    SELECT MAX(Salary * Months) FROM Employee
)