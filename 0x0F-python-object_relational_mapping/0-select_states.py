#!/usr/bin/python3

import sys
import MySQLdb

# Check if the number of arguments is correct
if len(sys.argv) != 4:
    print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
    sys.exit(1)

# Extract credentials
username, password, database = sys.argv[1:]

try:
    # Connect to MySQL database
    db = MySQLdb.connect(host="localhost",
                         user="root",
                         passwd="Phemmygmail@104",
                         db="hbtn_0e_0_usa",
                         port=3306)

    # Create a cursor object to execute queries
    cursor = db.cursor()

    # Execute SQL query to retrieve all states
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all rows from the result set
    rows = cursor.fetchall()[:5]

    # Print the list of states
    print("List of states:")
    for row in rows:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()

except MySQLdb.Error as e:
    print("MySQL Error:", e)
