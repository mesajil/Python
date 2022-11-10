class Pasajero:
    def __init__ (self, nombre, apellido, fecha):
        self.nombre = nombre
        self.apellido = apellido
        self.fecha = fecha

    def imprimir_detalle (self):
        print(f"Nombre: {self.nombre}")    
        print(f"Apellido: {self.apellido}")    
        print(f"Fecha de nacimiento: {self.fecha}")    


class Venta:
    def __init__ (self, pasajero, origen, destino, fecha, hora):
        self.pasajero = pasajero
        self.origen = origen
        self.destino = destino
        self.fecha = fecha
        self.hora = hora

    def imprimir_detalle (self):
        self.pasajero.imprimir_detalle()
        print(f"Ciudad origen: {self.origen}")
        print(f"Ciudad destino: {self.destino}")
        print(f"Fecha: {self.fecha}")
        print(f"Hora de salida: {self.hora}")


def menu ():
    print("\nMENU\n")
    print ("[1] Nueva venta de pasaje")
    print ("[2] Reporte de pasajes vendidos")
    print ("[3] Salir del programa\n")
    return input("Ingrese opción: ")


def crear_venta():
    
    # Leer ciudades.txt

    path = "D:\\Github\\Python\\U\\1\\ciudades.txt"
    ciudades = []
    with open(path, "r") as f:
        ciudades = [c.split("\n")[0] for c in f]
    
    # Pedir y guardar datos de venta

    path = "D:\\Github\\Python\\U\\1\\ventas.txt"
    with open(path, "a") as f:
        f.write(input("Nombre: ") + ",")
        f.write(input("Apellido: ") + ",")
        f.write(input("Fecha de nacimiento: ") + ",")
        
        # Pedir ciudad de origen y destino
        formato = [f"{i+1}:{c}" for i,c in enumerate(ciudades)] 
        while (1):
            origen = int(input(f"Seleccione Ciudad origen: {formato}: ")) - 1
            destino = int(input(f"Seleccione Ciudad destino: {formato}: ")) - 1
            if  valida_origendestino(origen, destino, ciudades): break
        
        f.write(ciudades[origen] + ",")
        f.write(ciudades[destino] + ",")
        f.write(input("Fecha: ") + ",")
        f.write(input("Hora de salida: ") + "\n")
        

def valida_origendestino(origen, destino, ciudades):
    return origen != destino and origen >= 0 and origen < len(ciudades) and destino >= 0 and destino < len(ciudades)


def reporte():

    ventas = leer_ventas()
    for v in ventas:
        print("\nDatos de la venta: ")
        v.imprimir_detalle ()


def leer_ventas():

    path = "D:\\Github\\Python\\U\\1\\ventas.txt"
    ventas = []
    with open(path, "r") as f:
        for c in f:
            data = c.split(",")
            p = Pasajero(data[0], data[1], data[2])
            v = Venta(p, data[3], data[4], data[5], data[6])
            ventas.append(v)
    return ventas



if __name__ == "__main__":
    while (1):
        opcion = menu()
        if opcion == "1": crear_venta()
        elif opcion == "2": reporte() 
        elif opcion == "3": break