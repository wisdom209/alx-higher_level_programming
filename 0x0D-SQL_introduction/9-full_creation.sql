-- create a table in given db
CREATE TABLE IF NOT EXISTS second_table (id INT NOT NULL AUTO_INCREMENT, name VARCHAR(256) NOT NULL, SCORE INT NOT NULL, PRIMARY KEY(id));
INSERT INTO second_table VALUES
(1, 'John', 10),
(2, 'Alex', 3),
(3, 'Bob', 14),
(4, 'George', 8);
