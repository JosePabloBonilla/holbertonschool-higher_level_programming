#!/usr/bin/python3
"""
Write a script that lists all states from the database hbtn_0e_0_usa
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
    cursor.execute("SELECT * FROM states ORDER BY states.id")
    states = cursor.fetchall()

    for i in states:
        print(i)

    cursor.close
    db.close
