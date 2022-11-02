class Pasajero:
    def __init__ (self, nombre, apellido, fecha):
        self.nombre = nombre
        self.apellido = apellido
        self.fecha = fecha

    def imprimir_detalle (self):
        print("Datos del pasajero: ")    
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
        print(f"Ciudad origen: {self.ciudad}")
        print(f"Ciudad destino: {self.destino}")
        print(f"Fecha: {self.destino}")
        print(f"Hora de salida: {self.destino}")


def menu ():
    print("MENU\n")
    print ("[1] Nueva venta de pasaje")
    print ("[2] Reporte de pasajes vendidos")
    print ("[3] Salir del programa\n")
    return input("Ingrese opción: ")


def vender_pasaje():
    
    # Leer ciudades.txt

    path = "D:\\Github\\Python\\U_Andres_Bello\\1\\ciudades.txt"
    ciudades = []
    with open(path, "r") as f:
        ciudades = [c.split("\n")[0] for c in f]
    
    # Pedir y guardar datos de venta

    path = "D:\\Github\\Python\\U_Andres_Bello\\1\\ventas.txt"
    with open(path, "a") as f:
        f.write(input("Nombre: ") + "\n")
        f.write(input("Apellido: ") + "\n")
        f.write(input("Fecha de nacimiento: ") + "\n")
        
        # Pedir ciudad de origen y destino
        formato = [f"{i+1}:{c}" for i,c in enumerate(ciudades)] 
        while (1):
            origen = int(input(f"Seleccione Ciudad origen: {formato}: ")) - 1
            destino = int(input(f"Seleccione Ciudad destino: {formato}: ")) - 1
            if  valida_origendestino(origen, destino, ciudades): break
        
        f.write(ciudades[origen] + "\n")
        f.write(ciudades[destino] + "\n")
        f.write(input("Fecha: ") + "\n")
        f.write(input("Hora de salida: ") + "\n")
        

def valida_origendestino(origen, destino, ciudades):
    return origen != destino and origen >= 0 and origen < len(ciudades) and destino >= 0 and destino < len(ciudades)


def reporte():

    ventas = leer_ventas()
    for v in ventas:
        v.imprimir_detalle ()


def leer_ventas():

    path = "D:\\Github\\Python\\U_Andres_Bello\\1\\ventas.txt"
    with open(path, "r") as f:
        pass



if __name__ == "__main__":
    while (1):
        opcion = menu()
        if opcion == "1": vender_pasaje()
        elif opcion == "2": reporte() 
        elif opcion == "3": break