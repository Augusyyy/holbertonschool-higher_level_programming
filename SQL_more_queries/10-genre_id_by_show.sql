
SELECT t.title, g.genre_id
FROM tv_shows AS t
INNER JOIN tv_show_genres AS g
ON t.id = g.show_id
ORDER BY t.title ASC, g.genre_id ASC;