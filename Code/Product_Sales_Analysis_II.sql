SELECT s.product_id, SUM(quantity) AS 'total_quantity'
FROM Sales s LEFT JOIN Product p
ON s.product_id = p.product_id
GROUP BY s.product_id;