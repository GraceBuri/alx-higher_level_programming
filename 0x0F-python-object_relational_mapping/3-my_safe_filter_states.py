#!/usr/bin/python3
"""display all values in state table"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)

    cursor = db.cursor()
    match = sys.argv[4]
    cursor.execute("SELECT * \
            FROM states \
            WHERE name LIKE BINARY %s \
            ", (match, ))
    states = cursor.fetchall()

    for state in states:
        print(state)
