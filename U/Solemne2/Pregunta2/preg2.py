import random
from functools import reduce

def main():

    # Inicializacion de listas
    animales = ["Perro", "Gato", "Gallina", "Oveja", "Vaca", "Cerdo"]
    nombres = ["Piggy", "Neron", "Margarita", "Manchitas", "Mimun", "Carlota"]
    
    # Crear lista combinada
    random.seed(5) # Definir una sola lista combinada
    random.shuffle(nombres) # Mezclar elementos de la lista de nombres 
    
    combinada = [[animales[i], nombres[i]] for i in range(len(animales))] # Combinamos listas
    
    menu = """
    OPCIONES

    [1] Indicar posicion
    [2] Indicar tipo de mascota que tiene el nombre con mas letras
    [3] Indicar tipo de mascota a partir de su nombre
    [0] Salir

        Ingrese opcion: """
    
    while (1):
        opcion = input(menu)
        print()
        match opcion:
            case "1": indicar_posicion(combinada)
            case "2": indicar_tipo_nombremaslargo(combinada)
            case "3": indicar_tipo_por_nombre(combinada)
            case "0": break



def indicar_posicion (combinada):
    """Indica la posicion de un mascota en la lista combinada
    para un nombre dado"""
    
    nombre = input("Ingrese nombre: ")
    
    for i, elemento in enumerate(combinada):
        if elemento[1] == nombre:
            print (f"Posicion: {i + 1}")
            break
    else:
        print("No se encontro una posicion")


def indicar_tipo_nombremaslargo (combinada):
    """Muestra el tipo de mascota con el nombre mas largo"""

    # tipo, _ = reduce(lambda e1,e2: e1 if len(e1[1]) >= len(e2[1]) else e2, combinada)
    maslargo = ""
    for elemento in combinada:
        if len(elemento[1]) > len(maslargo):
            tipo = elemento[0]
            maslargo = elemento[1]
    print (f"Tipo con nombre con mas letras: {tipo}")


def indicar_tipo_por_nombre(combinada):
    """Indica el tipo de mascota dado un nombre"""

    nombre = input("Ingrese nombre: ")
    
    for elemento in combinada:
        if elemento[1] == nombre:
            print (f"{nombre} es un(a) {elemento[0]}")
            break
    else:
        print("No se encontro el tipo de mascota")


if __name__ == "__main__":
    main()