-- 12. No genre
--  lists all shows contained in hbtn_0d_tvshows without a genre linked.

SELECT S.title AS title, SG.genre_id AS genre_id
  FROM tv_show_genres AS SG
 RIGHT JOIN tv_shows AS S ON SG.show_id = S.id
 WHERE SG.show_id IS NULL
 ORDER BY S.title, SG.genre_id;
