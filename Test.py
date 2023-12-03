from mysql.connector import connect, Error

def studentSelect(mydb):
	mycursor = mydb.cursor();
	query = "SELECT * FROM student"
	try:
		mycursor.execute(query);
		for result in mycursor.fetchall():
			print(result)
	except Error as e:
		print(e)

def selectStudentByName(mydb, name):
	mycursor = mydb.cursor();
	query = "SELECT * FROM student"
	query += "\nWHERE fname = \"" + name +"\""

	print(query)
	try:
		mycursor.execute(query);
		for result in mycursor.fetchall():
			print(result)
	except Error as e:
		print(e)

def insertNewStudent(mydb, fname, lname, gradeLevel, major):
	mycursor = mydb.cursor();
	query = """INSERT INTO student 
	(fname, lname, classStanding, major)
	VALUES"""
	values = fname, lname, gradeLevel, major
	query += str(values)
	print(query)
	try:
		mycursor.execute(query)
		mydb.commit()
		# for result in mycursor.fetchall():
		# 	print(result)
	except Error as e:
		print(e)

def createBookTable(mydb):
	mycursor = mydb.cursor();
	query = """
	DROP TABLE if exists Book;
	CREATE TABLE Book
	(
	bookID int primary key not null auto_increment,
	title VARCHAR(30),
	author VARCHAR(20)
	);	
	"""
	print(query)
	try:
		mycursor.execute(query, multi=True)
		# for result in mycursor.fetchall():
		# 	print(result)
	except Error as e:
		print(e)

def main():
	try:
		mydb = connect(
			host="localhost",
			user="root",
			password="Coding12@",   # Replace with yours
			database ="DS230"
		)

		#selectStudentByName(mydb, "Steve")
		insertNewStudent(mydb, "Homer", "Simpson", "Fr", "Nuc")
		studentSelect(mydb)
		createBookTable(mydb)

	except Error as e:
		print(e)
main()