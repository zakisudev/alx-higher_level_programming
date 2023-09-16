#!/usr/bin/python3
""" display states from the table by searching """
import MySQLdb
from sys import argv

if __name__ == "__main__":
    """ connect to db """
    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    """ create cursor """
    cur = db.cursor()
    cur.execute("""SELECT * FROM states WHERE name LIKE '{:s}'
                 ORDER BY id ASC""".format(argv[4]))
    for rec in cur.fetchall():
        if rec[1] == argv[4]:
            print(rec)
    cur.close()
    db.close()
