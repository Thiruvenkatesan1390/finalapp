import sqlite3

#Connecting to sqlite
conn = sqlite3.connect('tinku.db')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Retrieving data
cursor.execute('SELECT * from little_prince')

#Fetching 1st row from the table
result = cursor.fetchall();
print(result)

#Fetching 1st row from the table
result = cursor.fetchall();
print(result)

#Commit your changes in the database
conn.commit()

#Closing the connection
conn.close()
