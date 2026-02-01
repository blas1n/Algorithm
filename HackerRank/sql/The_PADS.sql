SELECT
    CONCAT(Name, '(', SUBSTRING(Occupation, 1, 1), ')')
FROM Occupations
ORDER BY Name, Occupation;

SELECT
    CONCAT('There are a total of ', COUNT(Occupation), ' ', LOWER(Occupation), 's.')
FROM Occupations
GROUP BY Occupation
ORDER BY COUNT(Occupation), Occupation;