import sqlite3
import datetime
import csv


def insert(roll_number, fname, lname, day, status):
    conn = sqlite3.connect("college.db")
    cur = conn.cursor()
    print(roll_number, fname, lname, day, status)
    cur.execute("INSERT INTO attendance VALUES (?,?,?,?,?)", (roll_number, fname, lname, day, status))
    conn.commit()
    conn.close()


def parse(csvfilename):
    """
     Reads csv file named csvfilename,parses
     its content and returns the data within
     the file as a list of lists
    """

    table = []
    with open(csvfilename, "r") as csvfile:
        for line in csvfile:
            line = line.rstrip()  # strips off the extra spaces(noise in data) in front & back
            columns = line.split(',')
            table.append(columns)
    return table


def feeddb(table):  # list of lists
    for col in table:
        a = int(col[0])  # extracted the roll_number
        b = str(col[1])
        c = str(col[2])
        d = (col[3].strip()).split('-')
        dy = int(d[0])
        mon = int(d[1])
        yr = int(d[2])
        d1 = datetime.date(yr, mon, dy)
        e = str(col[4])
        insert(a, b, c, d1, e)


table = parse("stu.csv")
feeddb(table)

