#!/usr/bin/python3
"""
a script that lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    """
    Retrives the states table from database
    """
    if len(sys.argv) != 5:
        print("Usage: script.py <username> <password> <database> <state_name>")
        sys.exit(1)
    
    try:
        db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                             port=3306, passwd=sys.argv[2], db=sys.argv[3])

        cursor = db.cursor()

        cursor.execute("SELECT * FROM states WHERE name LIKE BINARY '{}' \
                        ORDER BY states.id ASC".format(sys.argv[4]))

        data = cursor.fetchall()

        for row in data:
            print(row)

        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print("MySQL Error:", e)
        sys.exit(1)
