import sqlite3

#connection


conn = sqlite3.connect('tinku.db')
print("Opened database successfully");
conn.execute('CREATE TABLE little_prince(user_id INTEGER PRIMARY KEY,name TEXT NOT NULL,email TEXT NOT NULL UNIQUE ,password TEXT NOT NULL);')
print("Table created successfully");
