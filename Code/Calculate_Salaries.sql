SELECT s.company_id, s.employee_id, s.employee_name,
(CASE
WHEN maxS < 1000 THEN salary
WHEN maxS >= 1000 AND maxS <=10000 THEN ROUND(salary * (1 - 0.24))
ELSE ROUND(salary * (1 - 0.49))
 END) AS 'salary'
FROM Salaries s LEFT JOIN 
(SELECT company_id, MAX(salary) AS 'maxS' FROM Salaries GROUP BY company_id) m
ON s.company_id = m.company_id;