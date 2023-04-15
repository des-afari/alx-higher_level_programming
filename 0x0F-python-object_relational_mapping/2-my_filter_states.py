#!/usr/bin/python3
""" Lists all states from database hbtn_0e_0_usa by name """
import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = conn.cursor()

    cur.execute("SELECT * FROM states WHERE name='{}' ORDER BY id ASC"
                .format(argv[4]))
    rows = cur.fetchall()

    for row in rows:
        if row[1][:] == argv[4]:
            print(row)
    cur.close()
    conn.close()
