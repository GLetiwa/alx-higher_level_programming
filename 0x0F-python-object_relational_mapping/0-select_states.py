#!/usr/bin/python3
"""lists all states from the database hbtn_0e_0_usa"""
import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    cursor = None
    connection = None
    try:
        # connect to MySQL server
        connection = MySQLdb.connect(
                host='localhost',
                port=3306,
                user=username,
                passwd=password,
                db=database
            )
        # create a cursor
        cursor = connection.cursor()

        # SQL Querry to retrieve states
        cursor.execute("SELECT * FROM states ORDER BY id ASC")

        states = cursor.fetchall()
        for state in states:
            print(state)
    except MySQLdb.Error as e:
        print("Error connecting to MySQL: {}".format(e))

    finally:
        # close the cursor and connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()
