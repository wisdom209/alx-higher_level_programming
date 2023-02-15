-- list all cities name California
SELECT * FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California');
