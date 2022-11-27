"""
Pregunta 1
"""


def main():
    
    menu = """
    MENU

    [1] Nueva venta de pasaje
    [2] Reporte de pasajes vendidos
    [3] Salir del programa

        Ingrese opcion: """ # Texto del menu
    
    while (1):
        opcion = input(menu)
        match opcion:
            case "1": crear_venta()
            case "2": reporte()
            case "3": break


def crear_venta():
    
    # Leer ciudades
    with open(r"ciudades.txt", "r") as f:
        ciudades = [line.split("\n")[0] for line in f]
        print(ciudades)
    
    # Formateamos las ciudades para mostrarlas al usuario
    formato = [f"{i+1}:{c}" for i,c in enumerate(ciudades)]
    
    # Entrada de datos
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    nacimiento = input("Fecha de nacimiento: ")
    while (1):
        """Pedimos los indices de las ciudades de origen y destino al usuario"""
        origen = int(input(f"Seleccione Ciudad origen: {formato}: ")) - 1
        destino = int(input(f"Seleccione Ciudad destino: {formato}: ")) - 1
        if  valida_origendestino(origen, destino, ciudades):
            break
    fecha = input("Fecha: ")
    hora = input("Hora de salida: ")

    # Guardar datos de usuario
    datos = nombre, apellido,nacimiento,ciudades[origen],ciudades[destino],fecha,hora
    with open(r"ventas.txt", "a") as f:
        f.write(','.join(datos) + '\n') # Se guardan en una linea separados por comas


def valida_origendestino(origen, destino, ciudades):
    """Validamos que las indices de las ciudades esten en un rango
    y no sean iguales"""
    return origen in range(len(ciudades)) and destino in range(len(ciudades)) and origen != destino


def reporte():

    # Leer ventas
    with open(r"ventas.txt", "r") as f:
        """ventas es una lista de listas: cada elemento de "ventas"
        es una lista de datos por cada venta.
        Cada linea de texto es una cadena de datos separados por comas."""
        ventas = [line.split(",") for line in f]
    
    # Imprimir ventas
    for v in ventas:
        print(f"""
    Datos del pasajero:

    *   Nombre:                 {v[0]}
    *   Apellido:               {v[1]}
    *   Fecha de nacimiento:    {v[2]}

    Datos de la venta:

    *   Ciudad origen:          {v[3]}
    *   Ciudad destino:         {v[4]}
    *   Fecha:                  {v[5]}
    *   Hora de salida:         {v[6]}
    """)


if __name__ == "__main__":
    main()
