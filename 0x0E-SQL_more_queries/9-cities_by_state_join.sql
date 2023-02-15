-- list all cities in the database
SELECT DISTINCT cities.id AS id, cities.name AS name, states.name As name FROM cities INNER JOIN states ON cities.state_id = states.id;
