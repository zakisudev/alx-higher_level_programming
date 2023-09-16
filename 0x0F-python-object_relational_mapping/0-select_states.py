#!/usr/bin/python3
""" List all state in 'hbtn_0e_0_usa' database """


from sys import argv
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         database=argv[3])

    cur = db.cursor()
    cur.execute('SELECT * FROM states ORDER BY id ASC')

    for rec in cur.fetchall():
        print(rec)
