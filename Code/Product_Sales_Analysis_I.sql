SELECT product_name, year, price
FROM Sales s LEFT JOIN Product p
ON s.product_id = p.product_id;