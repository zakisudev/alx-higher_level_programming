#!/usr/bin/python3
""" fetch states starting with letter N """
import MySQLdb
from sys import argv
if __name__="__main__":
    """ connect to db """
    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=argv[1],
                         password=[2],
                         db=argv[3])
    """ create cursor """
    cur = db.cursor()
    cur.execute('SELECT *
                 FROM state
                 WHERE name LIKE 'N%'
                 ORDER BY id ASC')
    for rec in cur.fetchall():
        if row[1][0] == 'N':
            print(row)
    cur.close()
    db.close()
