import sqlite3


class Database:
    def __init__(self) -> None:
        pass
    with sqlite3.connect("app_users.db") as db:
        cursor = db.cursor()

    db.commit()

    def new_user():
        found = 0
        while found == 0:
            username = input("username: ")
            with sqlite3.connect("app_users.db") as db:
                cursor = db.cursor()
                finduser = ("SELECT * FROM app_users WHERE username = ?")
                cursor.execute(finduser, [(username)])
            if cursor.fetchall():
                print("username already in use :( try another one")
            else: 
                found = 1

        password = input("password: ")
        data = "INSERT INTO app_users (username, password) VALUES(?,?)"
        cursor.execute(data, [(username), (password)])
        db.commit()


    new_user()
    cursor.execute("Select * from app_users;")
    print(cursor.fetchall())

