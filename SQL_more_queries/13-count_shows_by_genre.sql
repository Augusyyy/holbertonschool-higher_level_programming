-- Lists all genres from the database hbtn_0d_tvshows along with the number of
SELECT g.name AS genre, COUNT(sg.show_id) AS number_of_shows
FROM tv_genres AS g
JOIN tv_show_genres AS sg
ON g.id = sg.genre_id
GROUP BY g.name
ORDER BY number_of_shows DESC;