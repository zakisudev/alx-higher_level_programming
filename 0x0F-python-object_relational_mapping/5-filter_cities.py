#!/usr/bin/python3
""" Print citis in a state from database """
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         database=argv[3])
    cur = db.cursor()
    state_name = argv[4]
    cur.execute("""SELECT c.name FROM cities AS c\
                INNER JOIN states AS s\
                ON c.state_id = s.id WHERE BINARY s.name\
                = BINARY %s ORDER BY c.id ASC""", (state_name,))
    records = []
    rows = cur.fetchall()
    for row in rows:
        records.append(row[0])
    print(", ".join(records))
    cur.close()
    db.close
