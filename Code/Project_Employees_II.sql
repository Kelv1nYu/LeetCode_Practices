SELECT project_id
FROM Project
GROUP BY project_id
HAVING COUNT(employee_id) = 
(SELECT COUNT(employee_id) AS 'cnt' 
FROM Project 
GROUP BY project_id 
ORDER BY cnt DESC 
LIMIT 1);