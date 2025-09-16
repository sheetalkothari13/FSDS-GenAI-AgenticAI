import mysql.connector

conn = mysql.connector.connect(host='localhost', user='root', password='2003')

if conn.is_connected():
    print("Connection successful")

print(conn)
print(conn.is_connected())


'''
===========
This script imports MySQL connector, tries to connect to a MySQL server running locally with username root and password 2003. If connected, it prints a success message, then prints the connection object and its status.
============
1) This imports the mysql.connector module. It’s a Python library that allows your Python code to connect and interact with MySQL databases.

2) This line creates a connection to your MySQL server. mysql.connector.connect() takes several arguments:
	host='localhost' → Means the database is running on your local machine.
	user='root' → Username for MySQL login (root is the default superuser).
	password='2003' → Password for that user.
The result is stored in the variable conn, which represents your connection object.

3) conn.is_connected() checks whether the connection to the database server was established successfully. If the connection exists, it prints "Connection successful".

4) This prints the connection object details (like host, user, database info).

5) Again checks if the connection is still active. Returns True if the connection is open, otherwise False.

'''