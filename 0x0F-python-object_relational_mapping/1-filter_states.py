#!/usr/bin/python3
"""0. Get all states"""

import MySQLdb
import sys

if __name__ == "__main__":

    db = MySQLdb.connect(
        host='localhost',
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
        )

    cur = db.cursor()

    sql = "select * from states where name like 'N%' order by id"

    cur.execute(sql)

    res = cur.fetchall()

    for x in res:
        print(x)

    cur.close()
    db.close()
