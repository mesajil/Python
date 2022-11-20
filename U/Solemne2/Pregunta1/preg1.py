def menu ():
    print("""
    MENU

    [1] Nueva venta de pasaje
    [2] Reporte de pasajes vendidos
    [3] Salir del programa

    """)

    return input("Ingrese opcion: ")


def crear_venta():
    
    datos = pedir_datos ()
    with open(r"ventas.txt", "a") as f:
        f.write(','.join(datos) + '\n')


def pedir_datos ():
    ciudades = leer_ciudades ()
    formato = [f"{i+1}:{c}" for i,c in enumerate(ciudades)]
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
    return nombre, apellido,fechanac,ciudades[origen],ciudades[destino],fecha,hora


def leer_ciudades ():
    with open(r"ciudades.txt", "r") as f:
        return [c.split("\n")[0] for c in f]


def valida_origendestino(origen, destino, ciudades):
    n = len(ciudades)
    return origen != destino and origen >= 0 and origen < n and destino >= 0 and destino < n


def reporte():

    ventas = leer_ventas()
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


def leer_ventas():

    with open(r"ventas.txt", "r") as f:
        return [line.split(",") for line in f]


def main():
    while (1):
        opcion = menu()
        match opcion:
            case "1": crear_venta()
            case "2": reporte()
            case "3": break


if __name__ == "__main__":
    main()