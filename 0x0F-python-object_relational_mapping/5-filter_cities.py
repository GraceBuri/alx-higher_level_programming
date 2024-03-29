#!/usr/bin/python3
"""list state name from user argument"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)

    cursor = db.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name \
            FROM cities \
            JOIN states ON cities.state_id = states.id\
            WHERE states.name = '{}';".format(sys.argv[4]))
    cities = cursor.fetchall()

    print(", ".join([city[1] for city in cities]))
