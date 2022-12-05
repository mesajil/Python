from .connection_db import ConnectionDB
from tkinter import messagebox


class Pelicula:
    def __init__ (self, nombre, duracion, genero):
        self.id_pelicula = None
        self.nombre = nombre
        self.duracion = duracion
        self.genero = genero


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


def guardar_registro (pelicula):
    connection = ConnectionDB()
    sql = f"""
    INSERT INTO peliculas (nombre, duracion, genero)
    VALUES ('{pelicula.nombre}', '{pelicula.duracion}', '{pelicula.genero}')
    """
    title = 'Guardar registro'
    try:
        connection.cursor.execute(sql)
        message = 'Se guardo el registro en la base de datos con exito.'
        messagebox.showinfo(title, message)
        connection.close_connection()
        return True
    except:
        message = 'La tabla peliculas no esta creada en la base de datos.'
        messagebox.showerror(title, message)
        connection.close_connection()
        return False


def listar_registros ():
    connection = ConnectionDB()
    sql = f"""
    SELECT * FROM peliculas
    """
    title = 'Listar registros'
    try:
        connection.cursor.execute(sql)
        return connection.cursor.fetchall()
    except:
        message = 'La tabla peliculas no esta creada en la base de datos.'
        messagebox.showerror(title, message)
    connection.close_connection()


def editar (pelicula, id_pelicula):
    connection = ConnectionDB()
    sql = f"""
    UPDATE peliculas
    SET nombre = '{pelicula.nombre}',
    duracion = '{pelicula.duracion}',
    genero = '{pelicula.genero}'
    WHERE id_pelicula = {id_pelicula}
    """
    try:
        connection.cursor.execute(sql)
        connection.close_connection()
    except:
        title = 'Edicion de datos'
        message = 'No se ha podido editar el registro.'
        messagebox.showerror(title, message)