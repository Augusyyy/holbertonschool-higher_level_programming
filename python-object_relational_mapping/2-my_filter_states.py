#!/usr/bin/python3
"""
displays all values in the states table 
of database where name matches the argument
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """
    init database
    """
    db = MySQLdb.connect(host="localhost",  port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    cursor = db.cursor()
    cursor.execute("SELECT `id`, `name` FROM `states`\
     WHERE `name` LIKE BINARY '{}' ORDER BY states.id ASC".format(argv[4]))
    rows = cursor.fetchall()

    for row in rows:
        print(row)
