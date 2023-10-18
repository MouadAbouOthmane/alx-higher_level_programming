-- 8. Cities of California
-- Lists all the cities of California that can be found in the database hbtn_0d_usa
SELECT C.id , C.name 
FROM cities as C, states as S 
WHERE S.name = 'California' AND C.state_id = S.id 
ORDER BY C.id;
