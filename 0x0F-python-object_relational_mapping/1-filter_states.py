#!/usr/bin/python3
"""This is filter module."""

import sys
import MySQLdb


def main():
    """Check correct number of arguments"""
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        return

    """Extract credentials."""
    username, password, database = sys.argv[1:]

    try:
        """Connect to MySQL database."""
        db = MySQLdb.connect(host="localhost",
                             user="root",
                             passwd="Phemmygmail@104",
                             db="hbtn_0e_0_usa",
                             port=3306)
        """Create cursor object."""
        cur = db.cursor()
        """Execute SQL query."""
        cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER\
                    BY id ASC")
        """Fetch all rows."""
        rows = cur.fetchall()
        """Print list of states."""
        print("List of states:")
        for row in rows:
            print(row)

        """Close cursor and database."""
        cur.close()
        db.close()
    except MySQLdb.Error as e:
        print("MySQL Error:", e)


if __name__ == "__main__":
    main()
