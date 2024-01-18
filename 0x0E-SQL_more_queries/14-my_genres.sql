-- Use database to list genre of the show
-- list the row of grnres in the database
SELECT name
FROM tv_genres
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
WHERE tv_shows.title = 'Dexter'
GROUP BY name
ORDER BY name ASC;
