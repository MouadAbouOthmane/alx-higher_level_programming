#!/usr/bin/python3
import MySQLdb

db = MySQLdb.connect(
    host='localhost',
    user='admin',
    passwd='root1234',
    db='hbtn_0e_0_usa'
    )

cur = db.cursor()

sql = "Select * from states"

cur.execute(sql)

res = cur.fetchall()

for x in res:
    print(x)
