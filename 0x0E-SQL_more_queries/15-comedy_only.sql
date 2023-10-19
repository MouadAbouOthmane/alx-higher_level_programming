-- 15. Only Comedy
-- Lists all Comedy shows in the database hbtn_0d_tvshows

SELECT S.title AS title
  FROM tv_genres AS G
 INNER JOIN tv_show_genres AS SG ON SG.genre_id = G.id
 INNER JOIN tv_shows AS S ON SG.show_id = S.id
 WHERE G.name = "Comedy"
 ORDER BY title;
 