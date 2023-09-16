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
    cursor.execute('SELECT *
                   FROM states
                   WHERE states.name=\'{}\'\
                   ORDER BY id ASC'.format(argSearch))
    for rec in cur.fetchall():
        if rec[1] == argSearch:
            print(cur)
    cur.close()
    db.close()
