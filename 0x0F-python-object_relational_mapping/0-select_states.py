#!/usr/bin/python3
""" list all states from the database 'hbtn_0e_0_usa' """
if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    """ connect to database """
    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=argv[1],
                         password=argv[2],
                         database=argv[3])
    """ create cursor """
    cur = db.cursor()
    cur.execute('SELECT*
                FROM states
                ORDER BY id DESC')
    """ display the record """
    for rec in cur.fetchall():
        print(rec)
    cur.close()
    db.close
