-- 14-my_genres.sql
-- Lists all genres of the show Dexter.

SELECT G.name AS name
  FROM tv_shows AS S
 INNER JOIN tv_show_genres AS SG ON S.id = SG.show_id
 INNER JOIN tv_genres AS G ON G.id = SG.genre_id
 WHERE S.title = "Dexter"
 ORDER BY name;
