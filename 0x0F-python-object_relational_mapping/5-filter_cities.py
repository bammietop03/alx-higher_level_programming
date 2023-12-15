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

    cursor.execute("SELECT cities.name \
                    FROM cities \
                    JOIN states \
                    ON cities.state_id = states.id \
                    WHERE states.name LIKE BINARY %s \
                    ORDER BY cities.id ASC", (argv[4],))

    data = cursor.fetchall()

    if data is not None:
        print(", ".join([row[0] for row in data]))

    cursor.close()
    db.close()
