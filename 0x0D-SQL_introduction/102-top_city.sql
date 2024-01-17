-- script that display the top 3 cities temperature during july and august

SELECT city, MAX(value) AS max_temperature
FROM hbtn_0c_0. temperatures
WHERE (month = 7 OR month = 8)
GROUP BY city
ORDER BY max_temperature DESC
LIMIT 3;
