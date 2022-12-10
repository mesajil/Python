from .connection import ConnectionDB

class Course:
    def __init__(self, title, description):
        self.title = title
        self.description = description


def create_courses_table ():
    connection = ConnectionDB()
    sql = """
    CREATE TABLE course (
        id_course INTEGER,
        title VARCHAR(100),
        description VARCHAR(200)
        PRIMARY KEY(id_pelicula AUTOINCREMENT)
    )
    """
    try:
        connection.cursor.execute(sql)
        connection.close_connection()
        print ('Se creo la tabla en la base de datos')
    except:
        print('La tabla ya esta creada.')


def delete_courses_table ():
    connection = ConnectionDB()
    sql = """
    DROP TABLE course
    """
    try:
        connection.cursor.execute(sql)
        connection.close_connection()
        print ('Tabla borrada.')
    except:
        print('No hay tabla para borrar.')


def create_course (course):
    connection = ConnectionDB()
    sql = f"""
    INSERT INTO course (title, description)
    VALUE (
        '{course.title}',
        '{course.description}'
        )
    """
    try:
        connection.cursor.execute(sql)
        connection.close_connection()
        print ("Se guardo el curso en la base de datos")
    except:
        print ("No se pudo crear el curso")


def read_course (id_course):
    connection = ConnectionDB()
    sql = f"""
    SELECT * FROM course
    WHERE id_course = {id_course}
    """

    try:
        connection.cursor.execute(sql)
        connection.close_connection()
        return connection.cursor.fetchall()
    except:
        print('La tabla peliculas no esta creada en la base de datos.')


def update_course (id_course, course):
    connection = ConnectionDB()
    sql = f"""
    UPDATE course
    SET title = '{course.title}',
    description = '{course.description}'
    WHERE id_course = {id_course}
    """
    try:
        connection.cursor.execute(sql)
        connection.close_connection()
        print(f'El curso {id_course} se actualizo con exito.')
    except:
        print ('No se ha podido editar el registro.')


def delete_course (id_course):
    connection = ConnectionDB()
    sql = f"""
    DELETE FROM course
    WHERE id_course = {id_course};
    """
    try:
        connection.cursor.execute(sql)
        connection.close_connection()
        print(f'La pelicula {id_course} has sido eliminada.')
    except:
        print('No se ha podido eliminar el registro.')

