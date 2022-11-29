from database_connection import get_database_connection

class User:
    def __init__(self, connection):
        self._connection = connection

    



user_rep = User(get_database_connection())