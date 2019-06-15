import sqlite3
import sys,datetime

roll_number = int(input("Enter roll no of a student : "))

def viewall(roll_number):
    conn = sqlite3.connect("college.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM attendance where roll_number=? ",(roll_number,))
    global data
    data = cur.fetchall()

def feedfile(data):
    f = open('details_for_a_student.csv','w')
    for row in data:
        for ele in row:
            f.write(str(ele))
            f.write(',')
        f.write('\n')
    f.close()
viewall(roll_number)
feedfile(data)
