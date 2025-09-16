import mysql.connector
conn = mysql.connector.connect(host='localhost', user='root', password='2003')

mycursor = conn.cursor()
mycursor.execute("Show databases")
for x in mycursor:
    print(x)   

'''
========
This script connects to MySQL using mysql.connector, creates a cursor, runs the SQL command "SHOW DATABASES", and prints each database name returned by the server. Essentially, it shows you all the databases that exist in your MySQL server.
========
1) Executes the SQL command "SHOW DATABASES".
	This command asks MySQL to list all the databases currently present on the server.

2) Iterates over the results returned by the query. Each x is a row from the result set. Since SHOW DATABASES returns one database name per row
''' 