-- Lists the number of fans per country origin of a band in descending order
SELECT origin, COUNT(fan_id) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
