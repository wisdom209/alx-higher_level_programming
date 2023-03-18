#!/usr/bin/env python3
"""Select States Module"""
import sys
import MySQLdb
if __name__ == '__main__':
    db_username = sys.argv[1]
    db_password = sys.argv[2]
    db_name = sys.argv[3]
    db_host = "localhost"
    state_name = sys.argv[4]

    db = MySQLdb.connect(user=db_username, password=db_password,
                         host=db_host, database=db_name)
    cursor = db.cursor()
    sqlquery = "SELECT cities.name FROM cities INNER JOIN states ON\
         cities.state_id = states.id WHERE states.name\
             LIKE BINARY %s ORDER BY cities.id ASC"
    cursor.execute(sqlquery, (state_name,))
    rows = cursor.fetchall()
    if rows is not None:
        for i in range(cursor.rowcount):
            if (i == cursor.rowcount - 1):
                print(rows[i][0])
            else:
                print(rows[i][0], end=", ")

    cursor.close()
    db.close()
