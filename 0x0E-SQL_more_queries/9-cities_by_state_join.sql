-- 9. Cities by States
-- Lists all cities contained in the database hbtn_0d_usa
SELECT C.id AS id, C.name AS name, S.name AS name
  FROM cities AS C, states AS S
 WHERE C.state_id = S.id
 ORDER BY C.id;
