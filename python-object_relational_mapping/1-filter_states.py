#!/usr/bin/python3
"""
lists all states with a name starting with N (upper N) from
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """
    init database
    """
    db = MySQLdb.connect(host="localhost", port=3306,user=argv[1],
                         passwd=argv[2], db=argv[3])

    cursor = db.cursor()
    cursor.execute("SELECT `id`, `name` FROM `states`\
     WHERE `name` LIKE 'N%' ORDER BY `id` ASC")
    rows = cursor.fetchall()

    for row in rows:
        print(row)
