#!/usr/bin/python3

import sys
import MySQLdb

# checks if the number of argument is correct
if len(sys.argv) != 4:
    print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
    sys.exit(1)
# Extract credentials
username, password, database = sys.argv[1:]

try:
    # connect to MySQL database
    db = MySQLdb.connect(host="localhost",
                        user="root",
                        passwd="root",
                        db="my_db",
                        port=3306)

    # create a cursor object to execute queries
    cursor = db.cursor()

    # Execute SQL query to retrieve all states
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # FETCH all rows from the result set
    rows = cursor.fetchall()

    # print the list of states
    print("List of states:")
    for row in rows:
        print("{}: {}".format(row[0], row[1]))

    # close cursor and database connection
    cursor.close()
    db.close()

except MySQLdb.Error as e:
    print("MySQL Error:", e)
