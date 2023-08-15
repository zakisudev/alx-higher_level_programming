-- Import hbtn_0c_0 and display top 3
SELECT city, AVG(value) AS avg_temp FROM temperatures WHERE month=7 OR month=8 GROUP BY avg_temp DESC LIMIT 3;
