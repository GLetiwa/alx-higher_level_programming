#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 5:
        sys.exit(1)

    username, password, database, state_name = sys.argv[1], sys.argv[2], \
        sys.argv[3], sys.argv[4]

    connection = None
    cursor = None

    try:
        # Connect to the MySQL server
        connection = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=username,
            passwd=password,
            db=database
        )

        cursor = connection.cursor()

        # Execute the SQL query to retrieve states
        query = "SELECT * FROM states WHERE name LIKE %s"
        cursor.execute(query, (state_name,))

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
