-- Uses the hbtn_0d_tvshows database
-- to list all genres of the show Dexter
SELECT name FROM tv_shows INNER JOIN
(tv_show_genres INNER JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id)
ON tv_shows.id = tv_show_genres.show_id
WHERE title='Dexter' ORDER BY name;
