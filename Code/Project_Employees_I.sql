SELECT project_id, ROUND(SUM(experience_years)/COUNT(p.employee_id), 2) AS 'average_years'
FROM Project p, Employee e
WHERE p.employee_id = e.employee_id
GROUP BY project_id;