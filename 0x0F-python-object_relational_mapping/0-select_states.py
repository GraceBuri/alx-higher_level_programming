#!/usr/bin/python3
"""list all states from hbtn_0e_0_usa"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states;")
    states = cursor.fetchall()

    for state in states:
        print(state)
