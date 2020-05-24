### Employees Earning More Than Their Managers

The `Employee` table holds all employees including their managers. Every employee has an Id, and there is also a column for the manager Id.
```
+----+-------+--------+-----------+
| Id | Name  | Salary | ManagerId |
+----+-------+--------+-----------+
| 1  | Joe   | 70000  | 3         |
| 2  | Henry | 80000  | 4         |
| 3  | Sam   | 60000  | NULL      |
| 4  | Max   | 90000  | NULL      |
+----+-------+--------+-----------+
```
Given the `Employee` table, write a SQL query that finds out employees who earn more than their managers. For the above table, Joe is the only employee who earns more than his manager.

```
+----------+
| Employee |
+----------+
| Joe      |
+----------+
```


####  Go to answer

[Employees_Earning_More_Than_Their_Managers.sql](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Code/Employees_Earning_More_Than_Their_Managers.sql)

#### Go to review

[Review Page](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/ReviewPage.md)