-- list all cities of california in the database hbtn_0d_usa

-- list all rows of a column in a database
SELECT id, name 
FROM cities 
WHERE state_id = (SELECT id FROM states WHERE name = 'california') 
ORDER BY id ASC;
