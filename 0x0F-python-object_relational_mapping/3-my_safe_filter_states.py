#!/usr/bin/python3
"""3. SQL Injection..."""

import MySQLdb
import sys

if __name__ == "__main__":

    db = MySQLdb.connect(
        host='localhost',
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
        )

    cur = db.cursor()

    sql = "select * from states where name = %s"

    cur.execute(sql, (sys.argv[4], ))

    res = cur.fetchall()

    for x in res:
        print(x)

    cur.close()
    db.close()
