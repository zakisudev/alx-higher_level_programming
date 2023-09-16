#!/usr/bin/python3
""" list all states from the database 'hbtn_0e_0_usa' """
from sys impoty argv
import MySQLdb

if __name__ == "__main__":
    """ connect to database """
    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=argv[1],
                         password=argv[2],
                         database=argv[3])
    cur = db.cursor()
    cur.execute('SELECT * FROM states ORDER BY id ASC')

    for rec in cur.fetchall():
        print(rec)
