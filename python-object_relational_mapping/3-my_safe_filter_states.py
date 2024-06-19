#!/usr/bin/python3
"""
write one that is safe from MySQL injections
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """
    init database
    """
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    with db.cursor() as cursor:
        cursor.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC",
                       (argv[4],))
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    cursor.close()
    db.close()
