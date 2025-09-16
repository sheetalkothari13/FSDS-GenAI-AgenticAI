import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="2003",
    database="mydatabase"
)

mycursor = conn.cursor()

sql = 'insert into customers (name, branch, id) values (%s, %s, %s)'

val = [
    ('Sheetal', 'CSE', 1),  
    ('Ankita', 'IT', 2),
    ('Riya', 'ECE', 3),
    ('Pooja', 'CSE', 4),
    ('Sonal', 'IT', 5)
]

mycursor.executemany(sql, val)
conn.commit()
print(mycursor.rowcount, "records inserted.")


'''
========
This script connects to the mydatabase database, prepares a parameterized INSERT statement, supplies five rows of data, inserts them efficiently using executemany(), commits the transaction, and prints the number of records inserted.
========

1) A parameterized SQL query string with placeholders (%s). Using placeholders avoids manual string concatenation and helps prevent SQL injection.
Note: for mysql.connector the placeholder is always %s regardless of the data type.

2) A Python list of tuples — each tuple holds the values for one row and matches the placeholder order in sql (name, branch, id).

3) Executes the INSERT once for every tuple in val. executemany is more efficient than looping single execute calls for many rows.
If an error occurs (e.g., duplicate primary key, constraint violation), execution may stop and raise an exception — consider wrapping in try/except.

4) Commits the current transaction so the inserted rows are persisted to the database. If you skip commit() (and autocommit is off), changes will not be saved.

5) Prints how many rows were affected by the last operation.
'''