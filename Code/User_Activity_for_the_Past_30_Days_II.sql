SELECT IFNULL(ROUND(AVG(sub.s), 2), 0) AS 'average_sessions_per_user'
FROM
(SELECT COUNT(DISTINCT session_id) AS 's'
 FROM Activity
 WHERE activity_date BETWEEN '2019-06-28' AND '2019-07-27'
 GROUP BY user_id) sub;