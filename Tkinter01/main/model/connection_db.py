import os
import sqlite3

class ConnectionDB:
    def __init__(self):
        self.open_connection ()
        self.cursor = self.connection.cursor()
    

    def open_connection (self):
        file_path = r"database/"
        try: os.mkdir(file_path)
        except FileExistsError: print ('Directory not created.')
        self.database = file_path + 'peliculas.db'
        self.connection = sqlite3.connect(self.database)


    def close_connection(self):
        self.connection.commit()
        self.connection.close()

    
