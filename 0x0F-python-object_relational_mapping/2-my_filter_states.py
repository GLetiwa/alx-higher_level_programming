#!/usr/bin/python3
"""
displays all values in the states table
where name matches the argument
"""
import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 5:
        sys.exit(1)
    username, password, database, state_name = sys.argv[1], sys.argv[2], \
        sys.argv[3], sys.argv[4]

    cursor = None
    connection = None

    try:
        connection = MySQLdb.connect(
                host='localhost',
                port=3306,
                user=username,
                passwd=password,
                db=database
            )

        cursor = connection.cursor()

        # Execute the SQL Query
        query = "SELECT * FROM states WHERE name \
                LIKE BINARY '{}'".format(state_name)
        cursor.execute(query)

        states = cursor.fetchall()

        for state in states:
            print(state)

    except MySQLdb.Error as e:
        print("Error connecting to MySQL: {}".format(e))

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
