-- 13. Number of shows by genre
--  Lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.

SELECT G.name AS genre, COUNT(SG.genre_id) AS number_of_shows
  FROM tv_show_genres AS SG
 INNER JOIN tv_genres AS G ON G.id = SG.genre_id
 GROUP BY G.name
 ORDER BY number_of_shows DESC; 
