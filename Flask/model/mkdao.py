from .connection import ConnectionDB

class Producto:
    def __init__(self, name, description):
        self.name = name
        self.description = description


def create_table ():
    connection = ConnectionDB()
    sql = """
    CREATE TABLE producto (
        id_producto INTEGER,
        name VARCHAR(100),
        description VARCHAR(200)
        PRIMARY KEY(id_producto AUTOINCREMENT)
    )
    """
    try:
        connection.cursor.execute(sql)
        connection.close_connection()
        print ('Se creo la tabla en la base de datos')
    except:
        print('La tabla ya esta creada.')


def delete_table ():
    connection = ConnectionDB()
    sql = """
    DROP TABLE producto
    """
    try:
        connection.cursor.execute(sql)
        connection.close_connection()
        print ('Tabla borrada.')
    except:
        print('No hay tabla para borrar.')


def create_producto (producto):
    connection = ConnectionDB()
    sql = f"""
    INSERT INTO producto (name, description)
    VALUE (
        '{producto.name}',
        '{producto.description}'
        )
    """
    try:
        connection.cursor.execute(sql)
        connection.close_connection()
        print ("Se guardo el curso en la base de datos")
    except:
        print ("No se pudo crear el curso")


def read_producto (id_producto):
    connection = ConnectionDB()
    sql = f"""
    SELECT * FROM producto
    WHERE id_producto = {id_producto}
    """

    try:
        connection.cursor.execute(sql)
        connection.close_connection()
        return connection.cursor.fetchall()
    except:
        print('La tabla peliculas no esta creada en la base de datos.')


def update_producto (id_producto, producto):
    connection = ConnectionDB()
    sql = f"""
    UPDATE producto
    SET name = '{producto.name}',
    description = '{producto.description}'
    WHERE id_producto = {id_producto}
    """
    try:
        connection.cursor.execute(sql)
        connection.close_connection()
        print(f'El curso {id_producto} se actualizo con exito.')
    except:
        print ('No se ha podido editar el registro.')


def delete_producto (id_producto):
    connection = ConnectionDB()
    sql = f"""
    DELETE FROM producto
    WHERE id_producto = {id_producto};
    """
    try:
        connection.cursor.execute(sql)
        connection.close_connection()
        print(f'La pelicula {id_producto} has sido eliminada.')
    except:
        print('No se ha podido eliminar el registro.')

