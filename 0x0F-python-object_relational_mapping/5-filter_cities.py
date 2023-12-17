#!/usr/bin/python3
"""Lists cities of a state"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
            user=sys.argv[1], passwd=sys.argv[2],
            db=sys.argv[3])

    cur = db.cursor()
    cur.execute("""SELECT cities.name FROM\
            cities INNER JOIN states ON states.id=cities.state_id\
            WHERE states.name=%s""", (sys.argv[4],))
    rows = cur.fetchall()
    temp = list(row[0] for row in rows)
    print(*temp, sep=", ")
    cur.close()
    db.close()
