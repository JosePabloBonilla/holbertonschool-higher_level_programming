#!/usr/bin/python3
"""
Write a script that lists all states with a name
starting with N (upper N) from the database hbtn_0e_0_usa:
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
    cursor.execute("SELECT * FROM states\
                    WHERE name LIKE 'N%'\
                    ORDER BY states,id")
    states = cursor.fetchall()

    for i in states:
        if i[1][0] == "N":
        print(i)

    cursor.close
    db.close
