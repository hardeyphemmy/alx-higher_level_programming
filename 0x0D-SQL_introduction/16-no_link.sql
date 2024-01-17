-- list all records of the 'second_table'
-- list name, display score in descending order

SELECT score, name
FROM second_table
HAVING name IS NOT NULL
ORDER BY score DESC;
