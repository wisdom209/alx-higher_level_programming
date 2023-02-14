-- script that displays the max temperature of each state (ordered by State name)
SELECT state, MAX(value) as max_tmp FROM temperatures GROUP BY state ORDER BY state;
