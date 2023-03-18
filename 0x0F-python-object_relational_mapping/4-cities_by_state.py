#!/usr/bin/python3
"""Select States Module"""
import sys
import MySQLdb
if __name__ == '__main__':
    db_username = sys.argv[1]
    db_password = sys.argv[2]
    db_name = sys.argv[3]
    db_host = "localhost"

    db = MySQLdb.connect(user=db_username, password=db_password,
                         host=db_host, database=db_name)
    cursor = db.cursor()
    sqlquery = "SELECT cities.id, cities.name, states.name FROM\
         cities INNER JOIN states ON cities.state_id = states.id"
    cursor.execute(sqlquery)
    rows = cursor.fetchall()
    for i in rows:
        print(i)
    cursor.close()
    db.close()
