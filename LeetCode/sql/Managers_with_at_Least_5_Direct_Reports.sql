SELECT manager.name FROM Employee manager
    LEFT JOIN Employee mentee ON manager.id = mentee.managerId
    GROUP BY manager.id HAVING COUNT(manager.id) >= 5