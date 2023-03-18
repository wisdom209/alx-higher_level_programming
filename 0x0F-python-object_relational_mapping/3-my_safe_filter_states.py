#!/usr/bin/env python3
"""Select States Module"""
import sys
import MySQLdb
if __name__ == '__main__':
    db_username = sys.argv[1]
    db_password = sys.argv[2]
    db_name = sys.argv[3]
    db_host = "localhost"
    state_name_searched = sys.argv[4]

    db = MySQLdb.connect(user=db_username, password=db_password,
                         host=db_host, database=db_name)
    cursor = db.cursor()
    sqlquery = "SELECT * FROM states WHERE name LIKE\
         BINARY {} ORDER BY id ASC".format('%s')
    cursor.execute(sqlquery, (state_name_searched,))
    rows = cursor.fetchall()
    for i in rows:
        print(i)
    cursor.close()
    db.close()
