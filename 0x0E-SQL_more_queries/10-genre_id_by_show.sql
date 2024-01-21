-- list all shows in hbtn_0d_tvshows that have atleast one genre linked
-- use hbtn_0d_tvshows
USE hbtn_0d_tv_shows;
-- list all rows in a column
SELECT tv_show.titles, tv_show_genres.genre_id
FROM tv_shows INNER JOIN tv_show_genres
ON tv_shows.id = tv_show_genre.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;