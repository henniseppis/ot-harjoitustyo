import os
import sqlite3

dirname = os.path.dirname(__file__)

with sqlite3.connect("test.db") as db:
    cursor = db.cursor()

cursor.execute('''create table users(username text primary key, password text);''')

def newUser():
    found=0
    while found == 0:
        username = input("Choose a username: ")
        with sqlite3.connect("test.db") as db:
            cursor= db.cursor()
            finduser = ("SELECT * FROM user WHERE username = ?")
            cursor.execute(finduser, [(username)])
        if cursor.fetchall():
            print("Username you chose is already in use:( Try another one")
        else: 
            found=1

newUser()

cursor.execute("SELECT * FROM user;")
print(cursor.fetchall())