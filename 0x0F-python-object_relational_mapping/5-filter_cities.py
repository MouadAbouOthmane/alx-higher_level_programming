#!/usr/bin/python3
"""5. All cities by state"""

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

    sql = "select c.name from states as s " \
        " inner join cities as c on c.state_id = s.id and s.name = %s"

    cur.execute(sql, (sys.argv[4], ))

    res = cur.fetchall()

    for i in range(len(res)):
        if i == len(res) - 1:
            print(res[i][0], end="")
        else:
            print(f"{res[i][0]}, ", end="")
    print()
    cur.close()
    db.close()
