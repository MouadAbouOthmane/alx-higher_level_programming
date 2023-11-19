#!/usr/bin/python3
import MySQLdb
import sys

db = MySQLdb.connect(
    host='localhost:3306',
    user=sys.argv[1],
    passwd=sys.argv[2],
    db=sys.argv[3]
    )

cur = db.cursor()

sql = "Select * from states"

cur.execute(sql)

res = cur.fetchall()

for x in res:
    print(x)
