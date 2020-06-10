SELECT
id,
MIN(CASE WHEN month = 'Jan' THEN revenue ELSE null END) AS Jan_Revenue,
MIN(CASE WHEN month = 'Feb' THEN revenue ELSE null END) AS Feb_Revenue,
MIN(CASE WHEN month = 'Mar' THEN revenue ELSE null END) AS Mar_Revenue,
MIN(CASE WHEN month = 'Apr' THEN revenue ELSE null END) AS Apr_Revenue,
MIN(CASE WHEN month = 'May' THEN revenue ELSE null END) AS May_Revenue,
MIN(CASE WHEN month = 'Jun' THEN revenue ELSE null END) AS Jun_Revenue,
MIN(CASE WHEN month = 'Jul' THEN revenue ELSE null END) AS Jul_Revenue,
MIN(CASE WHEN month = 'Aug' THEN revenue ELSE null END) AS Aug_Revenue,
MIN(CASE WHEN month = 'Sep' THEN revenue ELSE null END) AS Sep_Revenue,
MIN(CASE WHEN month = 'Oct' THEN revenue ELSE null END) AS Oct_Revenue,
MIN(CASE WHEN month = 'Nov' THEN revenue ELSE null END) AS Nov_Revenue,
MIN(CASE WHEN month = 'Dec' THEN revenue ELSE null END) AS Dec_Revenue
FROM Department
GROUP BY id;