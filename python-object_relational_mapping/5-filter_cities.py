#!/usr/bin/python3
"""
lists all cities of that state
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """
    Access to the database and get the cities
    """
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    with db.cursor() as cursor:
        cursor.execute("SELECT id,name FROM cities \
                    WHERE state_id IN \
                    (SELECT id FROM states WHERE name = %(state_name)s)",
                       {'state_name': argv[4]})
        rows = cursor.fetchall()
    if rows is not None:
        print(", ".join([row[1] for row in rows]))
