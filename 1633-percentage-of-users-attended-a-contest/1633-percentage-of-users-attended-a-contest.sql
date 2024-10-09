# Write your MySQL query statement below
SELECT contest_id, ROUND((COUNT(user_id) / LENGTH(contest_id) * 100), 2) AS percentage
FROM Register
GROUP BY contest_id
ORDER BY percentage DESC, contest_id;