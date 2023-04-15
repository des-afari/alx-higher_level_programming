#!/usr/bin/python3
"""List all states with a name starting with N"""

if __name__ == '__main__':
    import MySQLdb
    from sys import argv

    conn = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = conn.cursor()

    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' \
    ORDER BY id ASC")
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()
