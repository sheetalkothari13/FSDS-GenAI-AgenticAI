import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="2003",
    database="mydatabase"
)

mycursor = conn.cursor()
mycursor.execute("CREATE TABLE customers (name VARCHAR(255), branch VARCHAR(255), id int)")
mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)
    
    
'''
=======
This script connects to the MySQL server (using root login) and works inside the database mydatabase. It then creates a table called customers with three columns (name, branch, id). After that, it runs SHOW TABLES to list all the tables in mydatabase and prints them out.
=======

1) Creates a cursor object from the connection. A cursor is used to send SQL commands and fetch results from the server.

2) Sends an SQL command to the database to create a new table named customers.The table has 3 columns:
	name → text field, up to 255 characters.
	branch → text field, up to 255 characters.
	id → integer field.

3)Executes the SQL command "SHOW TABLES". This lists all the tables available in the current database (mydatabase).

4) Iterates over the result set from SHOW TABLES. Each x is a tuple containing one table name.
'''










