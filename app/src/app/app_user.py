class User:
    def __init__(self):
        self.users = {}

    def add_user(self):
        while True:
            user_name = str(input("Choose username: "))
            password = str(input("Choose password: "))

            if not user_name in self.users:
                self.users[user_name] = password
                print("User created")
                break
            else:
                print("Username already in use, please choose another one")
