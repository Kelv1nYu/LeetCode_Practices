**175. [Combine_Two_Tables.sql](https://github.com/Kelv1nYu/LeetCode_Practices/blob/master/Code/Combine_Two_Tables.sql)**      Level: Easy

中文：

* 使用LEFT JOIN进行表的合并。LEFT JOIN 会返回左表的一切值且只返回与左表有交集的右表值，若无匹配返回空值。
* 在合并表时，通常使用 ON 来指定需要根据哪组列值进行合并，但若标志列名字相同，也可以使用 USING。


English:
* Using LEFT JOIN to combine two tables. The MySQL LEFT OUTER JOIN would return the all records from table1 and only those records from table2 that intersect with table1.
* In general, we use ON in MySQL. In Joins, we use ON in a set of columns. USING is useful when both the tables share a column of the exact same name on which they join.