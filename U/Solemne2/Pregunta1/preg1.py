"""
Solemne 02 Pregunta 1


"""

####################################################
#           Funcion Crear venta
####################################################

def crear_venta():
    
    # Lectura de datos
    with open(r"ciudades.txt", "r") as f:
        ciudades = [line.split("\n")[0] for line in f]
    
    # Proceso
    formato = [f"{i+1}:{c}" for i,c in enumerate(ciudades)]
    
    # Entradas: nombre, apellido, fechanac, origen, destino, fecha y hora
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    fechanac = input("Fecha de nacimiento: ")
    while (1):
        origen = int(input(f"Seleccione Ciudad origen: {formato}: ")) - 1
        destino = int(input(f"Seleccione Ciudad destino: {formato}: ")) - 1
        if  valida_origendestino(origen, destino, ciudades):
            break
    fecha = input("Fecha: ")
    hora = input("Hora de salida: ")

    # Escribir datos
    datos = nombre, apellido,fechanac,ciudades[origen],ciudades[destino],fecha,hora
    with open(r"ventas.txt", "a") as f:
        f.write(','.join(datos) + '\n')


####################################################
#           Funcion validar origen y destino
####################################################

def valida_origendestino(origen, destino, ciudades):
    # Salidas
    return origen in range(len(ciudades)) and destino in range(len(ciudades)) and origen != destino


####################################################
#           Funcion Reporte de pasajes vendidos
####################################################

def reporte():

    # Leer datos
    with open(r"ventas.txt", "r") as f:
        ventas = [line.split(",") for line in f]
    
    # Salidas
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


####################################################
#           Funcion principal
####################################################

def main():
    
    # Inicializar
    menu = """
    MENU

    [1] Nueva venta de pasaje
    [2] Reporte de pasajes vendidos
    [3] Salir del programa

        Ingrese opcion: """
    
    while (1):
        
        # Entradas
        opcion = input(menu)
        
        # Proceso
        match opcion:
            case "1": crear_venta()
            case "2": reporte()
            case "3": break

    # Salida: Fin del programa


####################################################
#           Punto de entrada
####################################################

if __name__ == "__main__":
    main()
    # Salida: Fin del programa
