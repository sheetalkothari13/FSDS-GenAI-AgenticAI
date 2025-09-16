import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="2003"
)

if conn.is_connected():
    print("Connection successful")

mycursor = conn.cursor()
mycursor.execute("CREATE DATABASE mydatabase")
print(mycursor)



'''
=========
This script connects to a local MySQL server as user root, checks the connection, opens a cursor, executes a CREATE DATABASE SQL statement to create mydatabase, and prints the cursor object.
=========
1) import mysql.connector
	Loads the mysql.connector Python package so you can talk to a MySQL server from Python.
	This module provides connect(), Cursor objects, and methods to execute SQL.

2) Calls mysql.connector.connect() to open a connection to the MySQL server.
	host="localhost" → connect to a MySQL server on the same machine.
	user="root" → the MySQL username.
	password="2003" → the password for that user.
The function returns a connection object (stored in conn) that you use to create cursors and run SQL.

3) If True, the code prints the confirmation message. This is a simple runtime sanity check.

4) mycursor = conn.cursor()
	Creates a cursor object from the connection. A cursor is the interface used to execute SQL statements and fetch results.

5) mycursor.execute("CREATE DATABASE mydatabase")
	Runs the SQL statement CREATE DATABASE mydatabase on the server. That creates a new database named mydatabase.
	If a database with that name already exists, MySQL will raise an error (e.g., “database exists”) unless you use CREATE DATABASE IF NOT EXISTS mydatabase.

6) print(mycursor)
	Prints a Python representation of the cursor object (something like 	<mysql.connector.cursor_cext.CMySQLCursor object at 0x...>).
	This does not show the result of the CREATE DATABASE command. It only prints the cursor object. To verify the database creation, query SHOW DATABASES and fetch results.

'''