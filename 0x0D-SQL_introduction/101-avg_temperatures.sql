-- display the average temperature (Farenhite)
--  by city ordered by temperature (descending).
SELECT `city`, AVG(`value`) AS `average_temperature`
FROM `temperatures`
GROUP BY `city`
ORDER BY `average_temperature` DESC;
