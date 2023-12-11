from mysql.connector import connect, Error
import csv
import numpy as np
import random

def createSchedule(mydb):
    mycursor = mydb.cursor();
    query = """
    DROP TABLE if exists Schedule;
    CREATE Table Schedule
    (
    courseID INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
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
    studentID INT,
    studentNumber INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
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
    courseID INT,
    status  ENUM('Active', 'Waitlist', 'Complete'),
    classSize INT (100),
    primary key (studentID,courseID)
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
    (title,instructor, days, begtime, endtime,bldgRoom,credits,year,term)
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

def insertNewStudent(mydb, studentID, fname, lname, classYear, Major1, Major2, Minor1,Advisor):
    mycursor = mydb.cursor();
    query = """Insert into Student
       (studentID,fname ,lname ,classYear,Major1,Major2 ,Minor1 ,Advisor)
        values """
    values = studentID, fname, lname, classYear, Major1, Major2, Minor1,Advisor
    query += str(values)
    query += ";"
    print(query)
    try:
        mycursor.execute(query)
        mydb.commit()
        for result in mycursor.fetchall():
            print(result)
    except Error as e:
        print(e)

def populateEnrollment(mydb):
    enrollStudent(mydb, "1242", "164")
    enrollStudent(mydb, "1242", "2")
    enrollStudent(mydb, "1242", "22")
    enrollStudent(mydb, "1242", "39")
    enrollStudent(mydb, "1252", "164")
    enrollStudent(mydb, "1252", "68")
    enrollStudent(mydb, "1252", "86")
    enrollStudent(mydb, "1252", "117")
    enrollStudent(mydb, "1262", "164")
    enrollStudent(mydb, "1262", "115")
    enrollStudent(mydb, "1262", "112")
    enrollStudent(mydb, "1262", "138")
    enrollStudent(mydb, "1272", "164")
    enrollStudent(mydb, "1272", "237")
    enrollStudent(mydb, "1272", "277")
    enrollStudent(mydb, "1272", "326")
    enrollStudent(mydb, "1282", "164")
    enrollStudent(mydb, "1282", "237")
    enrollStudent(mydb, "1282", "277")
    enrollStudent(mydb, "1282", "326")
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

def DCPlookup(mydb):
    mycursor = mydb.cursor();

    query = """
    select * 
    from Schedule 
    where SUBSTRING(title,8,1) = "7" ;
    
    select * 
    from Schedule 
    where SUBSTRING(title,8,1) = "6" ;

    select * 
    from Schedule 
    where SUBSTRING(title,8,1) = "8" ;
    
    """


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





def getStudentID(mydb,lname):
    mycursor = mydb.cursor();
    query = """
    select studentID
    from Student
    where lname = 
    """
    query += "\"" + lname + "\""
    print(query)
    try:
        mycursor.execute(query);
        for result in mycursor.fetchall():
            print(result)
    except Error as e:
        print(e)

def getCourseID(mydb,title):
    mycursor = mydb.cursor();
    query =  """
    select courseID
    from schedule
    where title =
    """
    query += "\"" + title + "\""
    print(query)
    try:
        mycursor.execute(query);
        for result in mycursor.fetchall():
            print((result[0]))
    except Error as e:
        print(e)

def aliasgetCourseID(mydb,title):
    mycursor = mydb.cursor();
    m = ""
    query =  """
    select courseID
    from schedule
    where title like 
    """
    if title[-1] == "W":
        title = title[:-4]
    query += "\"" + title + "%\""
    #print(query)
    try:
        mycursor.execute(query);
        for result in mycursor.fetchall():
            return (result[0])
    except Error as e:
        print(e)

def enrollStudent(mydb,sID,cID):
    mycursor = mydb.cursor();
    status = "Active"
    cSize = "100"
    query = """
    Insert into Enrollment
	    (studentID,courseID,status,classSize)
	    values
	    (
	    """
    query += "\"" + sID + "\","
    query += "\"" + cID + "\","
    query += "\"" + status + "\","
    query += "\"" + cSize + "\");"
    print(query)
    try:
        mycursor.execute(query)
        mydb.commit()
        for result in mycursor.fetchall():
            print(result)
    except Error as e:
        print(e)


def anonymize(mydb):
    aliases = {}
    idnums = []
    lname = []
    fname = []
    Class = []
    major1 = []
    major2 = []
    minor = []
    advisor = []
    generateID = random.randint(10000000,19999999)

    #print(generateID , "Generated")
    with open('Registration.csv') as infile:
        csvFile = csv.reader(infile)
        header = next(csvFile)
        for line in csvFile:
            if (len(line[0]) == 8):
                idnums.append(line[0])
                lname.append(line[1])
                fname.append(line[2])
                Class.append(line[3])
                major1.append(line[4])
                major2.append(line[5])
                minor.append(line[6])
                advisor.append(line[7])


        #print(idnums,lname,fname)
        #generatename = random.randint(0, len(idnums) - 1)
        for i in range (len(idnums)):
            t = random.randint(10000000,19999999)
            tt = lname[random.randint(0, len(idnums) - 1)]
            ttt = fname[random.randint(0, len(idnums) - 1)]
            if idnums[i] not in aliases:
                aliases[idnums[i],lname[i],fname[i]] = t, tt, ttt
               # insertNewStudent(mydb, t, ttt, tt, Class[i], major1[i], major2[i], minor[i], advisor[i])

    return aliases

def enrollAliases(mydb):
    alises = anonymize(mydb)

    with open('Registration.csv') as infile:
        currentclass = ""
        csvFile = csv.reader(infile)
        header = next(csvFile)
        currclass = (next(csvFile))
        currentclass = currclass.pop()
        currentclass = aliasgetCourseID(mydb,currentclass)
        for line in csvFile:
            if (len(line[0]) > 8 ):
                currentclass = aliasgetCourseID(mydb,line[0])
            else:
                for key in alises:
                    if key[0] == line[0]:
                        enrollStudent(mydb,str(alises[key][0]),str(currentclass))



def listStudent(mydb): #This Function shows you all your students with their ID numbers in alphabetical order by the lastname
    mycursor = mydb.cursor();
    query = """
    select studentID,fname,lname 
    from student
    order by lname, fname;
    """
    #print(query)
    try:
        mycursor.execute(query);
        for result in mycursor.fetchall():
            print(result)
    except Error as e:
        print(e)

def studentLookup(mydb,idnum): #This lets you look up and find all the students information by just by the id number
    mycursor = mydb.cursor();
    query = """
        select *
    from student
    where studentID ="""
    query += idnum
    #print(query)
    try:
        mycursor.execute(query);
        for result in mycursor.fetchall():
            print(result)
    except Error as e:
        print(e)

def instructorClasses(mydb,instructor): #This lets you find all the classes a instructor is teaching
    mycursor = mydb.cursor();
    query = """
        select *
    from schedule
    where instructor =
    """
    query += "\"" + instructor + "\""
    print(query)
    try:
        mycursor.execute(query);
        for result in mycursor.fetchall():
            print(result)
    except Error as e:
        print(e)




#This function shows you the ID, first and last name of every student who is taking the class
def takingClass(mydb,title):
    mycursor = mydb.cursor();
    query = """
       select studentID
from enrollment
where courseID = 7
       """
    print(query)
    try:
        mycursor.execute(query);
        for result in mycursor.fetchall():
            print(result)
    except Error as e:
        print(e)




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
        #instructorClasses(mydb,"S Hughes")
        #studentLookup(mydb,"1242")
        #listStudent(mydb)
        #enrollAliases(mydb)
        #aliasgetCourseID(mydb,"AAM  137  01   W")
        #anonymize(mydb)
        #populateEnrollment(mydb)
        #insertNewStudent(mydb,'1242',"David","Lukula","Jr","CS","","DS","Hughes")
        #insertNewStudent(mydb,"1252","Chris","Baker","Jr","CS","","DS","Hughes")
        #insertNewStudent(mydb,"1262","Cael","Schmitt","Sr","CS","","DS","Hughes")
        #insertNewStudent(mydb,'1272',"Stephen","Hooghs","Fr","CS","PSY","ANT","Hughes")
        #insertNewStudent(mydb,'1282',"John","Doe","So","CS","PHY","DS","Hughes")
        #createEnrollment(mydb)
        #createStudent(mydb)
        #profLookup(mydb,"S Harmsen")
        #courseTime(mydb,"10:00 AM")
        #courseDept(mydb,"AAM")
        #DCPlookup(mydb)
        #createSchedule(mydb)
        #for i in range(len(titles)):
            #insertNewClass(mydb,titles[i],instructor[i],days[i],begtime[i],endtime[i],bldgRoom[i],creditz[i])
             #myinfo = (titles[i], instructor[i], days[i], begtime[i], endtime[i], bldgRoom[i], creditz[i])
    except Error as e:
        print(e)

main()

