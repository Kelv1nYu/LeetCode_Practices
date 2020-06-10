SELECT name
FROM salesperson
WHERE sales_id NOT IN
(SELECT sales_id FROM orders o JOIN company c ON o.com_id = c.com_id WHERE c.name = 'RED');