import os
import sqlite3

class ConnectionDB:
    def __init__(self):
        self.open_connection ()
        self.cursor = self.connection.cursor()
    

    def open_connection (self):
        file_path = r"database/"
        try: os.mkdir(file_path) # Crear directorio
        except FileExistsError: pass
        self.database = file_path + 'cursos.db'
        self.connection = sqlite3.connect(self.database)


    def close_connection(self):
        self.connection.commit()
        self.connection.close()