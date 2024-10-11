SELECT activity_date AS day, COUNT(DISTINCT session_id) AS active_users
FROM Activity
WHERE activity_date >= DATE_SUB('2019-07-27', INTERVAL 29 DAY)
  AND activity_date <= '2019-07-27'
GROUP BY activity_date
HAVING active_users >= 1 ;