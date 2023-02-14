-- export an sql dump and then run a query to find average 
-- temperatures in a city, grouping by cities in descending
-- temperature order
SELECT city, AVG(value) AS avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
