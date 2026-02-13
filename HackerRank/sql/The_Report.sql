SELECT
    IF(g.Grade >= 8, s.Name, NULL),
    g.Grade,
    s.Marks
FROM Students s
LEFT JOIN Grades g ON s.Marks >= g.Min_Mark AND s.Marks <= MAX_Mark
ORDER BY Grade DESC, Name