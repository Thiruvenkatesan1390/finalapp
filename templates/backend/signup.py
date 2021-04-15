import create
import ins
import sqlite3

#for login
#def login():
def signup():
    while True:
        email = input("Please enter your email:");
        password = input("Please enter your password:");
       # with sqlite3.connect("mecproject.db") as db:
        with sqlite3.connect("tinku.db") as db:
            cursor = db.cursor()
        find_user = ("SELECT * FROM little_prince WHERE email = ? AND password = ?")
        cursor.execute(find_user, [(email), (password)])
        results = cursor.fetchall()
        break
signup()

'''  if results:
            for i in results:
               print("welcome " + i[1])
            break
        else:
            print("Invalid user")
            again = input("Do you want to try again?(Y/N):")
            if again.lower() == "n":
                print("good bye")
                break'''


#login()
