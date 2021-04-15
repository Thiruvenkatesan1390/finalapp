import sqlite3

#insertion

conn = sqlite3.connect('tinku.db')
#conn.execute("INSERT INTO little_princess(first_name,last_name,email,password,phone)VALUES('anushkhash','viratko','1234@gmail.com','181818','0000000004')");
#conn.execute("INSERT INTO little_princess(first_name,last_name,email,password,phone)VALUES('benita','sam','1254@gmail.com','545454','0000000054')");
#conn.execute("INSERT INTO little_princess(first_name,last_name,email,password,phone)VALUES('anushkhash','viratko','12345@gmail.com','100000','0000000004')");
#conn.execute("INSERT INTO little_princess(first_name,last_name,email,password,phone)VALUES('benny','samantha','1000@gmail.com','54545410','0000000065')");
#conn.execute("INSERT INTO little_prince(name,email,password)VALUES('anu','1200@gmail.com','testing1')");

conn.execute("INSERT INTO little_prince(name,email,password)VALUES('anu','120@gmail.com','testing1')");
conn.commit()

print("Records created successfully");
conn.close()
