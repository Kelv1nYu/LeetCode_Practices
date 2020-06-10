SELECT class
FROM (SELECT DISTINCT student, class FROM courses) sub
GROUP BY class
HAVING COUNT(*) >= 5;