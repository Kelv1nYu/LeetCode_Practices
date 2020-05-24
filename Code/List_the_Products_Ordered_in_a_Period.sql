SELECT p.product_name, SUM(o.unit) AS 'unit'
FROM Products p, Orders o
WHERE p.product_id = o.product_id
AND MONTH(o.order_date) = 02
AND YEAR(o.order_date) = 2020
GROUP BY p.product_name
HAVING SUM(o.unit) >= 100