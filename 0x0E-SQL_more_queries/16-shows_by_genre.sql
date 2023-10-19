-- 16. List shows and genres
-- Lists all shows, and all genres linked to that show, from the database

SELECT S.title AS title, G.name AS name
  FROM tv_genres AS G
 LEFT JOIN tv_show_genres AS SG ON SG.genre_id = G.id
 RIGHT JOIN tv_shows AS S ON SG.show_id = S.id
 ORDER BY title, name;
 