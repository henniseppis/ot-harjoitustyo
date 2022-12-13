import sqlite3
from database_connection import get_database_connection

class User:
    def __init__(self):
        pass 

    def new_user():
        found = 0
        while found == 0:
            username = input("username: ")
            with sqlite3.connect("users_harjoitus.db") as db:
                cursor = db.cursor()
                finduser = ("SELECT * FROM users WHERE username = ?")
                cursor.execute(finduser, [(username)])
            if cursor.fetchall():
                print("username already in use :( try another one")
            else: 
                found = 1
    
        password = input("password: ")
        data = "INSERT INTO users (username, password) VALUES(?,?)"
        cursor.execute(data, [(username), (password)])
        db.commit()
   
    def login():
        pass
    
   
User().new_user()