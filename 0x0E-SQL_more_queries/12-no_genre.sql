-- list all shows database in hbtn_0d_tvshows
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows LEFT JOIN tv_shows.genre
ON tv_shows.id = tv_show_genres.show_id
WHERE tv_shows_genres.genre_id IS NULL
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
