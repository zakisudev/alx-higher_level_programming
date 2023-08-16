-- List all shows by their rating

SELECT tv_shows.title, SUM(rate) AS rating
FROM tv_shows
JOIN tv_show_ratings ON tv_shows.id=tv_show_ratings.show_id
GROUP By tv_shows.id
ORDER BY rating DESC;
