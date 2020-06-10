SELECT MIN(ABS(p2.x - p1.x)) AS 'shortest'
FROM point p1 JOIN point p2
ON p1.x != p2.x;