#!/usr/bin/python3
""" Print citis in a state from database """
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         port=3306             
                         user=argv[1],
                         passwd=argv[2],
                         database=argv[3])
    cur = db.cursor()
    state_name = argv[4]
    cur.execute("SELECT ct.name"
                "FROM cities AS ct"
                "INNER JOIN states AS st"
                "ON ct.state_id"
                "WHERE BINARY st.name = BINARY %s"
                "ORDER BY ct.id ASC", (state_name))
    records = []
    rows = cur.fetchall()
    for row in rows:
        records.append(row[0])
    print(", ".join(records))
    cur.close()
    db.close
