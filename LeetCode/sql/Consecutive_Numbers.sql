SELECT DISTINCT l1.num as ConsecutiveNums FROM Logs l1, Logs l2, Logs l3
WHERE l1.num = l2.num and l1.num = l3.num and l1.id + 1 = l2.id and l2.id + 1 = l3.id