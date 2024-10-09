SELECT query_name, 
       ROUND(SUM(rating / position) / COUNT(*), 2) AS quality,
       ROUND((SELECT COUNT(*) FROM Queries WHERE rating < 3 AND query_name = Q.query_name) 
            / COUNT(*) * 100, 2) AS poor_query_percentage 
FROM Queries Q
WHERE query_name IS NOT NULL
GROUP BY query_name;