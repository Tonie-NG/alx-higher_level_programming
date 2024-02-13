-- a script that displays the average temperature (Fahrenheit)
SELECT `city`,  AVG(`VALUE`) AS `avg_temp`
FROM `temperatures`
GROUP BY `city`
ORDER BY `avg_temp` DESC;
