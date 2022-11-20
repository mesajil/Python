import random
from functools import reduce

def generar_listacombinada ():

    animales = ["Perro", "Gato", "Gallina", "Oveja", "Vaca", "Cerdo"]
    nombres = ["Piggy", "Nerón", "Margarita", "Manchitas", "Mimun", "Carlota"]
    random.shuffle(nombres)
    return [[animales[i], nombres[i]] for i in range(len(animales))]


def menu():
    
    print("""
    OPCIONES

    [1] Indicar posicion
    [2] Indicar tipo de mascota que tiene el nombre con mas letras
    [3] Indicar tipo de mascota a partir de su nombre
    [0] Salir

    """)
    
    return input("Ingrese opcion: ")


def indicar_posicion (combinada):

    nombre = input("Ingrese nombre: ")
    nombres = [nombre for _, nombre in combinada]
    try:
        index = nombres.index(nombre)
        print (f"Posicion: {index + 1}")
    except:
        print("No se encontro una posicion")


def indicar_tipo_nombremaslargo (combinada):

    nombres = [nombre for _, nombre in combinada]
    nombremaslargo = reduce(lambda x,y: x if len(x) >= len(y) else y, nombres)
    index = nombres.index(nombremaslargo)
    print (f"Tipo con nombre con mas letras: {combinada[index][0]}")


def indicar_tipo_por_nombre(combinada):

    nombre = input("Ingrese nombre: ")
    nombres = [nombre for _, nombre in combinada]
    try:
        index = nombres.index(nombre)
        print (f"{nombre} es un(a) {combinada[index][0]}")
    except:
        print("No se encontro el tipo de mascota")


def main():

    combinada = generar_listacombinada()
    while (1):
        opcion = menu()
        match opcion:
            case "1": indicar_posicion(combinada)
            case "2": indicar_tipo_nombremaslargo(combinada)
            case "3": indicar_tipo_por_nombre(combinada)
            case "0": break


if __name__ == "__main__":
    main()