import mysql.connector as mysql
db = mysql.connect(
 host = "localhost",
 user = "root",
 passwd = "827519",
 database="Institute_ST_student"  ## write this after the database is create in line 14
)
 

print(db)  
# Creating the data base
cursor = db.cursor()

# cursor.execute("CREATE DATABASE Institute_ST_student")  ##delete this after creating the database
cursor.execute("SHOW DATABASES")
database= cursor.fetchall()

print(database)

#Create table Beginers_python 
# cursor.execute("CREATE TABLE Beginers_python(id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, Name VARCHAR(255), User_name VARCHAR(255), Email VARCHAR(255))")
# cursor.execute("CREATE TABLE Advance_python(id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, Name VARCHAR(255), User_name VARCHAR(255), Email VARCHAR(255), Beginer VARCHAR(255))")

## fetch tables
cursor.execute("DESC Beginers_python")

print(cursor.fetchall()) 

# cursor.execute("DROP DATABASE Institute_ST_student ")

## inserting data into both tables
query = "INSERT INTO Beginers_python (Name, User_name, Email) VALUES (%s,%s, %s)"

 ## storing values in a variable
values =[
 ("Zakaria", "Zac", "zac_bgn@ist.ac.ke"),
("Eric", "Eric.pc", "ericpc_bgn@ist.ac.ke"),
("joseph", "JoTrevor", "joTrevor_bgn@ist.ac.ke"),
("Hennah", "Scovia", "scovia_bgn@ist.ac.ke"),
("Darunga", "Darunga", "darung_bgn@ist.ac.ke"),
("Moses", "Moze", "mozeg_bgn@ist.ac.ke"),
("Brayo", "Brayn", "brayn_bgn@ist.ac.ke"),
("Joy", "Joy", " joy_bgn@ist.ac.ke"),
("Hayat", "nany", "nanyshan_bgn@ist.ac.ke"),
("Godfrey", "Degenius", "degeniusbgn@ist.ac.ke")
]

## executing the query with values
cursor.executemany(query, values)

db.commit()
print(cursor.rowcount, "records inserted")

query = "SELECT * FROM Beginers_python"


# ## getting records from the table
cursor.execute(query)

# ## fetching all records from the 'cursor' object
records = cursor.fetchall()

# ## Showing the data
for record in records:
 	print(record)

## getting 'user_name' column from the table
query_1="select User_name FROM Beginers_python"
cursor.execute(query_1)

# ## fetching all usernames from the 'cursor' object
usernames = cursor.fetchall()

# ## Showing the data
for username in usernames:
	print(username)
# cursor.execute("DROP TABLE Advance_python") use this to delete the empty table.

#update specific data from the table
## defining the Query
query = "UPDATE Beginers_python SET Name = 'Sam' WHERE id = 1"

## executing the query
cursor.execute(query)

## final step to tell the database that we have changed the table data
db.commit()
cursor.close()
