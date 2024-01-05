#!/usr/bin/python3
"""
a script that lists all cities from the database hbtn_0e_0_usa
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """
    Retrives the cities table from database
    """
    db = MySQLdb.connect(host="localhost", user=argv[1],
                         port=3306, passwd=argv[2], db=argv[3])

    cursor = db.cursor()

    cursor.execute("SELECT cities.id, cities.name, states.name \
                    FROM cities, states \
                    WHERE cities.state_id = states.id \
                    ORDER BY cities.id ASC")

    data = cursor.fetchall()

    for row in data:
        print(row)

    cursor.close()
    db.close()
