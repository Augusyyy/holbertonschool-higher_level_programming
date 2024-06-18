#!/usr/bin/python3
"""
This script that lists all cities from the database hbtn_0e_0_usa
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
        cursor.execute("SELECT cities.id, cities.name, states.name\
                        FROM cities\
                        LEFT JOIN states ON cities.state_id = states.id\
                        ORDER BY cities.id ASC")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    cursor.close()
    db.close()