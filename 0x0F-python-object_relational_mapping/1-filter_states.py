#!/usr/bin/python3
""" fetch states starting with letter N """
import MySQLdb
from sys import argv

if __name__ == "__main__":
    """ connect to db """
    database = MySQLdb.connect(host='localhost',
                               port=3306,
                               user=argv[1],
                               passwd=argv[2],
                               db=argv[3])
    """ create cursor """
    cur = database.cursor()
    cur.execute('SELECT * FROM states ORDER BY id ASC')
    for rec in cur.fetchall():
        if rec[1][0] == 'N':
            print(rec)
    cur.close()
    database.close()
