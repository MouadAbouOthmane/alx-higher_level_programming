-- 11. Genre ID for all shows
-- Lists all shows contained in hbtn_0d_tvshows If a show doesn’t have a genre, display NULL.
SELECT S.title AS title, SG.genre_id AS genre_id
  FROM tv_show_genres AS SG
 RIGHT JOIN tv_shows AS S ON S.id = SG.show_id 
 ORDER BY S.title, SG.genre_id;
