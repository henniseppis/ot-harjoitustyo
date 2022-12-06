import sqlite3

class New_user:
    with sqlite3.connect("users_database") as db:
        cursor = db.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users(username VARCHAR NOT NULL, password VARCHAR NOT NULL)''')
    
    cursor.execute('''INSERT INTO users (username, password) values ("hennzzu", "blää")''')
    
    db.commit()
    
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
    
    
    new_user()
    cursor.execute("Select * from app_users;")
    print(cursor.fetchall())
    
    