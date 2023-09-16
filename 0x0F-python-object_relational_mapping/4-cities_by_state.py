#!/usr/bin/python3
""" fetch all cities """
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cur = db.cursor()
    query = """SELECT cities.id, cities.name, states.name\
            FROM cities\
            JOIN states\
            ON cities.state_id = states.id\
            ORDER BY cities.id ASC"""
    cur.execute(query)
    for rec in cur.fetchall():
        print(rec)
