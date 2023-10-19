-- 10-genre_id_by_show.sql
-- Lists all shows contained in hbtn_0d_tvshows that have at least one genre linked
SELECT S.title AS title, SG.genre_id AS genre_id
  FROM tv_genres AS G, tv_show_genres AS SG, tv_shows AS S
 WHERE G.id = SG.genre_id AND S.id = SG.show_id
 ORDER BY S.title, SG.genre_id;
