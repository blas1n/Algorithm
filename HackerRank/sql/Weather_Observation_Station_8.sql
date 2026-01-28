SELECT DISTINCT City FROM Station
WHERE City REGEXP '^[aeiou]' and City REGEXP '[aeiou]$'