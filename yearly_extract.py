import sqlite3
import sys,datetime

roll_number = int(input("Enter roll no of a student : "))
year = int(input("Enter year : "))

def viewall(roll_number,year):
    sdate = datetime.date(year,1,1)
    edate = datetime.date(year,12,31)
    conn = sqlite3.connect("college.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM attendance where roll_number=? and day>=? and day<=?",(roll_number,sdate,edate))
    global data
    data = cur.fetchall()

def feedfile(data):
    f = open('student_details_for_a_year.csv','w')
    for row in data:
        for ele in row:
            f.write(str(ele))
            f.write(',')
        f.write('\n')
    f.close()
viewall(roll_number,year)
feedfile(data)
