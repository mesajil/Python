import sqlite3

class ConnectionDB:
    def __init__(self):
        self.database = 'database/peliculas.db'
        self.connection = sqlite3.connect(self.database)
        self.cursor = self.connection.cursor()
    
    def close_connection(self):
        self.connection.commit()
        self.connection.close()

    
