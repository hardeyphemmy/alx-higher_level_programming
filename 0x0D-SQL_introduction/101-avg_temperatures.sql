-- script that display average temperature by city ordered by temp.
-- convert celcius to fahrenheit: (celcius * 9/5) +32

SELECT
    city,
    AVG((value * 9/5) +32) AS average_temperature_fahrenheit
FROM
    temperatures
GROUP BY
    city
ORDER BY
    average_temperatures_fahrenheit DESC;
