-- List all shows not linked to the Dexter show

SELECT tv_genres.name
FROM tv_genres
WHERE tv_genres.id NOT IN(
SELECT tv_show_genres.genre_id
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id=tv_show_genres.show_id
where tv_shows.title='Dexter')
ORDER BY tv_genres.name ASC;
