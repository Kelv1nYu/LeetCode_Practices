SELECT d.Name AS 'Department', e.Name AS 'Employee', Salary
FROM Employee e JOIN Department d
ON e.DepartmentId = d.Id
WHERE (e.DepartmentId, Salary) IN
(SELECT DepartmentId, MAX(Salary) FROM EMployee GROUP BY DepartmentId)