import sqlite3
from sqlite3 import Error


# connection


def login():
    try:
        while True:
            email = input("Please enter your email:");
            password = input("Please enter your password:");

            with sqlite3.connect("user_details.db") as db: #db = sqlite3.connect("user_details.db"
                cursor = db.cursor()
            find_user = ("SELECT * FROM accounts_details WHERE email = ? AND password = ?")
            cursor.execute(find_user, [(email), (password)])
            results = cursor.fetchall()

            if results:
                for i in results:
                    print("welcome " + i[1])
                break
            else:
                print("Invalid user")
                again = input("Do you want to try again?(Y/N):")
                if again.lower() == "n":
                    print("good bye")
                    break
    except Error as e:
        print(e)

    finally:
        db.close()
