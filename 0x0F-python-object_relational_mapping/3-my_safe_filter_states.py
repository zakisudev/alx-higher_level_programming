#!/usr/bin/python3
""" display states from the table by searching """
import MySQLdb
from sys import argv
if __name__ == "__main__":
    """ connect to db """
    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=argv[1],
                         password=argv[2],
                         db=argv[3])
    """ create cursor """
    cur = db.cursor()
    query = """SELECT * FROM states WHERE name = %s ORDER BY id ASC"""
    cur.execute(query, (argv[4],))
    for rec in cur.fetchall():
        print(rec)
    cur.close()
    db.close()
