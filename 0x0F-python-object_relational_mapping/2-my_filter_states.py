#!/usr/bin/python3
""" Filter states based on argument """
import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3],
                           host="localhost", port=3306)
    cur = conn.cursor()

    cur.execute("SELECT * FROM states WHERE name='{}' \
    OREDER BY id ASC".format(argv[4]))
    rows = cur.fetchall()

    for row in rows:
        if row[1][:] == argv[4]:
            print(row)

    cur.close()
    conn.close()
