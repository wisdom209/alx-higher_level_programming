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

    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    rows = cursor.fetchall()

    for i in rows:
        print(i)
    cursor.close()
    db.close()
