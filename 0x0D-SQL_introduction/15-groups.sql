-- list number of records with the same score in the 'second_table'
-- display the score with label

SELECT score, COUNT(1) AS number FROM second_table
GROUP BY score
GROUP BY number DESC;
