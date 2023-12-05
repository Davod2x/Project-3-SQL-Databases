from mysql.connector import connect, Error
import csv
import numpy as np

def createSchedule(mydb):
    mycursor = mydb.cursor();
    query = """
    DROP TABLE if exists Schedule;
    CREATE Table Schedule
    (
    title VARCHAR(50),
    instructor VARCHAR(20),
    days VARCHAR(3),
    begtime VARCHAR(10),
    endtime VARCHAR(10),
    bldgRoom VARCHAR(20),
    credits VARCHAR(5),
    year VARCHAR(4),
    term VARCHAR(6)
    );	
    """
    print(query)
    try:
        mycursor.execute(query, multi=True)
        # for result in mycursor.fetchall():
        # 	print(result)
    except Error as e:
         print(e)

def createStudent(mydb):
    mycursor = mydb.cursor();
    query = """
    DROP TABLE if exists STUDENT;
    CREATE TABLE STUDENT
    (
    studentID INT PRIMARY KEY NOT NULL,
    studentNumber INT NOT NULL,
    fname VARCHAR(20),
    lname VARCHAR(20),
    classYear  ENUM('Fr', 'So', 'Jr', 'Sr'),
    Major1 VARCHAR(20),
    Major2 VARCHAR(20),
    Minor1 VARCHAR(20),
    Advisor VARCHAR(20)
    
);	
    """
    print(query)
    try:
        mycursor.execute(query, multi=True)
        # for result in mycursor.fetchall():
        # 	print(result)
    except Error as e:
         print(e)


def createEnrollment(mydb):
    mycursor = mydb.cursor();
    query = """
    DROP TABLE if exists ENROLLMENT;
    CREATE TABLE ENROLLMENT
    (
    studentID INT,
    courseID INT PRIMARY KEY NOT NULL,
    status  ENUM('Active', 'Waitlist', 'Complete'),
    classSize INT (100)
    );	
    """
    print(query)
    try:
        mycursor.execute(query, multi=True)
        # for result in mycursor.fetchall():
        # 	print(result)
    except Error as e:
        print(e)

def insertNewClass(mydb, title, instructor, days, begtime, endtime, bldgRoom, credits):
    year = "2021"
    term = "Fall"
    mycursor = mydb.cursor();
    query = """INSERT INTO Schedule 
    (title, instructor, days, begtime, endtime,bldgRoom,credits,year,term)
    VALUES"""
    values = title, instructor, days, begtime, endtime, bldgRoom, credits,year,term
    query += str(values)
    print(query)
    try:
        mycursor.execute(query)
        mydb.commit()
        for result in mycursor.fetchall():
            print(result)
    except Error as e:
        print(e)


def courseDept(mydb,dept):
    mycursor = mydb.cursor();
    leng = len(dept)
    if leng == 2:
        query = " select * from Schedule where SUBSTRING(title,1,2)  ="
        query += "\""+ dept +"\""
    if leng == 3:
        query = " select * from Schedule where SUBSTRING(title,1,3)  ="
        query += "\""+ dept +"\""
    print(query)
    try:
        mycursor.execute(query);
        for result in mycursor.fetchall():
            print(result)
    except Error as e:
        print(e)

def courseTime(mydb,starttime):
    #Format HH:MM AM/PM
    mycursor = mydb.cursor();
    query = "select * from Schedule where Schedule.begtime  ="
    query += "\"" + starttime + "\""
    print(query)
    try:
        mycursor.execute(query);
        for result in mycursor.fetchall():
            print(result)
    except Error as e:
        print(e)


def profLookup(mydb,profName):
    mycursor = mydb.cursor();
    query = "select * from Schedule where instructor ="
    query += "\"" + profName + "\""
    print(query)
    try:
        mycursor.execute(query);
        for result in mycursor.fetchall():
            print(result)
    except Error as e:
        print(e)

def generateStudents(mydb):
    mycursor = mydb.cursor();
    query = """
    Insert into Student
        (studentID ,studentNumber ,fname ,lname ,classYear,Major1,Major2 ,Minor1 ,Advisor)
        values
        ('1242','1',"David","Lukula","Jr","CS","","DS","Hughes"),
        ("1252","2","Chris","Baker","Jr","CS","","DS","Hughes"),
        ("1262","3","Cael","Schmitt","Sr","CS","","DS","Hughes"),
        ('1272','4',"Stephen","Hooghs","Fr","CS","PSY","ANT","Hughes"),
        ('1282','5',"John","Doe","So","CS","PHY","DS","Hughes");
        
        
    Insert into Enrollment
	(studentID,courseID,status,classSize)
	values
    ('1242',"1","Active",100),
    ('1242',"2","Active",100),
    ('1242',"3","Active",100),
    ('1242',"4","Active",100),
    ("1252","5","Active",100),
    ("1252","2","Active",100),
    ("1252","3","Active",100),
    ("1252","6","Active",100),
    ("1262","1","Active",100),
    ("1262","3","Active",100),
	("1262","5","Active",100),
    ("1262","7","Active",100),
	("1272","8","Active",100),
	("1272","2","Active",100),
	("1272","6","Active",100),
	("1272","3","Active",100);
    
    
    """

def main():
    titles = []
    instructor = []
    days = []
    begtime = []
    endtime = []
    bldgRoom = []
    creditz = []

    myinfo = ()


    with open('Course Schedule.csv') as infile:
        csvFile = csv.reader(infile)
        header = next(csvFile)
        for lines in csvFile:
            #print (lines)
            titles.append(lines[0])
            instructor.append(lines[1])
            days.append(lines[2])
            begtime.append(lines[3])
            endtime.append(lines[4])
            bldgRoom.append(lines[5])
            creditz.append(lines[6])






    try:

        mydb = connect(
            host="localhost",
            user="root",
            password="Coding12@",  # Replace with yours
            database="Project3"
        )
        #createEnrollment(mydb)
        #createStudent(mydb)
        #profLookup(mydb,"S Harmsen")
        #courseTime(mydb,"10:00 AM")
        #courseDept(mydb,"AAM")
        #createSchedule(mydb)
        #for i in range(len(titles)):
             #insertNewClass(mydb,titles[i],instructor[i],days[i],begtime[i],endtime[i],bldgRoom[i],creditz[i])
             #myinfo = (titles[i], instructor[i], days[i], begtime[i], endtime[i], bldgRoom[i], creditz[i])
    except Error as e:
        print(e)

main()
