USE hbtn_0d_tvshows;

-- Get shows with the genre Comedy
SELECT show_id
FROM tv_show_genres
JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_genres.name = 'Comedy';

-- List all shows without the genre Comedy
SELECT tv_shows.title
FROM tv_shows
WHERE id NOT IN (
	    SELECT show_id
	    FROM tv_show_genres
	    JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
	    WHERE tv_genres.name = 'Comedy'
)
ORDER BY tv_shows.title ASC;
