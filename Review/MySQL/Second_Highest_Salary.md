**176. [Second_Highest_Salary.sql](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Code/Second_Highest_Salary.sql)**      Level: Easy

中文：

* 对薪资进行降序排列并使用LIMIT查找出第二高的工资，并对其进行再次查询。
* 通过使用IFNULL或使用临时表来应对第二高的工资为空的情况。
* 另注：LIMIT 1,1 的含义是跳过第一条读取一条信息，而 LIMIT 1 OFFSET 1 的含义为从第一条开始（不包含第一条）读取一条信息。

English:
* Sort the distinct salary in descend order and then utilize the LIMIT clause to get the second highest salary.
* To solve the 'NULL' problem, we can use IFNULL function or take the result of query as a temp table.
* Note: `LIMIT 1,1` means to skip the first one to read one message, and `LIMIT 1 OFFSET 1` means to read one message from the first (not including the first).