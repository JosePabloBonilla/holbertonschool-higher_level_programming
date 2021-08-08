#!/usr/bin/python3
"""
Write a script that takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument.
"""


if __name__ == '__main__':
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(user=argv[1],
                         passwd=argv[2],
                         database=argv[3],
                         host="localhost",
                         port=3306)

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'".format(argv[4]))
    states = cursor.fetchall()

    for i in states:
        print (i)

    cursor.close
    db.close
