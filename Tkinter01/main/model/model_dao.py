from .connection_db import ConnectionDB
from tkinter import messagebox

def crear_tabla ():
    connection = ConnectionDB()
    sql = """
    CREATE TABLE peliculas (
        id_pelicula INTEGER,
        nombre VARCHAR(100),
        duracion VARCHAR(10),
        genero VARCHAR(100),
        PRIMARY KEY(id_pelicula AUTOINCREMENT)
    )
    """
    try:
        connection.cursor.execute(sql)
        title = 'Crear tabla'
        message = 'Se creo la tabla en la base de datos'
        messagebox.showinfo(title, message)
    except:
        title = 'Crear tabla'
        message = 'La tabla ya esta creada.'
        messagebox.showwarning(title, message)
    connection.close_connection()


def borrar_tabla ():
    connection = ConnectionDB()
    sql = """
    DROP TABLE peliculas
    """
    try:
        connection.cursor.execute(sql)
        title = 'Borrar tabla'
        message = 'La tabla de la base de datos se borro con exito.'
        messagebox.showinfo(title, message)
    except:
        title = 'Borrar tabla'
        message = 'No hay tabla para borrar.'
        messagebox.showerror(title, message)
    connection.close_connection()