#!/usr/bin/python3
"""
a script that lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """
    Retrives the states table from database
    """
    if len(argv) != 5:
        raise Exception("Usage: python script.py <username> <password> <database> <state_name>")

    db = MySQLdb.connect(host="localhost", user=argv[1],
                         port=3306, passwd=argv[2], db=argv[3])

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY '{}' \
                    ORDER BY states.id ASC".format(argv[4]))

    data = cursor.fetchall()

    for row in data:
        print(row)

    cursor.close()
    db.close()
