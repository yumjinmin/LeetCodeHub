# Write your MySQL query statement below
SELECT W1.id
FROM Weather as W1, Weather as W2
WHERE DATEDIFF(W1.recordDate, W2.recordDate) = 1 and W1.temperature > W2.temperature;
# W1이 W2의 하루 뒤, 온도가 더 높음
