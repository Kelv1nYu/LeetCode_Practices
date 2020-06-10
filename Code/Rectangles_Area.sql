
SELECT po1.id AS 'p1', po2.id AS 'p2', (ABS(po1.x_value-po2.x_value) * ABS(po1.y_value-po2.y_value)) AS 'area'
FROM Points po1 , Points po2
WHERE po1.id < po2.id
AND po1.x_value != po2.x_value
AND po1.y_value != po2.y_value
ORDER BY area DESC, p1 ASC, p2 ASC;