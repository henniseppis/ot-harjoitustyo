from database_connection import get_database_connection

class Create_Database:

    def __init__(self):
        self.connection = get_database_connection()
    

    def drop_tables(self):
        cursor = self.connection.cursor()

        cursor.execute("DROP TABLE IF EXISTS app_users")

        self.connection.commit()


    def create_tables(self):
        cursor = self.connection.cursor()

        cursor.execute('''CREATE TABLE app_users
                (username text NOT NULL,
                password text NOT NULL);''')

        self.connection.commit()
        cursor.close()


    def initialize_database(self):
        connection = get_database_connection()

        self.drop_tables()
        self.create_tables()


if __name__ == "__main__":
    Create_Database().initialize_database()
