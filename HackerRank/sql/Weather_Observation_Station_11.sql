SELECT DISTINCT City FROM Station
WHERE City REGEXP '^[^aeiou]' or City REGEXP '[^aeiou]$'