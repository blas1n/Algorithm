SELECT e.name, b.bonus FROM Employee e
    LEFT JOIN Bonus b ON e.empId = b.empId
    WHERE b.Bonus IS NULL or b.Bonus < 1000
