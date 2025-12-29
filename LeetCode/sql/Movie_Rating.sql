(SELECT name as results FROM Users u
JOIN MovieRating r ON u.user_id = r.user_id
GROUP BY name
ORDER BY COUNT(r.rating) DESC, u.name LIMIT 1)
UNION ALL
(SELECT title as results FROM Movies m
JOIN MovieRating r ON m.movie_id = r.movie_id
WHERE YEAR(r.created_at) = 2020 and MONTH(r.created_at) = 2
GROUP BY title
ORDER BY AVG(r.rating) DESC, m.title LIMIT 1)