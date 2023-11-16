-- Get genres linked to the show Dexter
USE hbtn_0d_tvshows;

SELECT genre_id
FROM tv_show_genres
JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title = 'Dexter';

-- List all genres not linked to the show Dexter
SELECT tv_genres.name
FROM tv_genres
WHERE id NOT IN (
	    SELECT genre_id
	    FROM tv_show_genres
	    JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
	    WHERE tv_shows.title = 'Dexter'
)
ORDER BY tv_genres.name ASC;
