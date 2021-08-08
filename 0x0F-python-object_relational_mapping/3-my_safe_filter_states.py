#!/usr/bin/python3
"""
Wait, do you remember the previous task? Did you test "Arizona';
TRUNCATE TABLE states ; SELECT * FROM states WHERE name = '" as an input?
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
                    WHERE name LIKE %s\
                    ORDER BY states.id", (argv[4],))

    states = cursor.fetchall()

    for i in states:
        print (i)

    cursor.close
    db.close
