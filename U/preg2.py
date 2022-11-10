
import random
from functools import reduce

def menu():
    
    print("\nOPCIONES\n")
    print ("[1] Indicar posición")
    print ("[2] Indicar tipo de mascota que tiene el nombre con más letras")
    print ("[3] Indicar tipo de mascota a partir de su nombre")
    print ("[0] Salir \n")
    
    return input("Ingrese opción: ")


def indicar_posicion (nombres):

    nombre = input("Ingrese nombre: ")
    try:
        index = nombres.index(nombre) + 1
        print (f"Posición: {index}")
    except:
        print("No se encontró una posición")


def indicar_tipo (animales, nombres):

    largo = reduce(lambda a,b: a if len(a) >= len(b) else b, nombres)
    index = nombres.index(largo)
    print (f"Tipo con nombre con más letras: {animales[index]}")


def indicar_tipo_por_nombre(animales, nombres):

    nombre = input("Ingrese nombre: ")
    try:
        index = nombres.index(nombre)
        print (f"{nombre} es un(a) {animales[index]}")
    except:
        print("No se encontró el tipo de mascota")

if __name__ == "__main__":

    # Generar lista combinada

    animales = ["Perro", "Gato", "Gallina", "Oveja", "Vaca", "Cerdo"]
    nombres = ["Piggy", "Nerón", "Margarita", "Manchitas", "Mimun", "Carlota"]
    random.shuffle(nombres)
    combinada = [[animales[i], nombres[i]] for i in range(len(animales))]
    print(f"Lista combinada: {combinada}")

    # Menu principal

    while (1):
        opcion = menu()
        if opcion == "1": indicar_posicion(nombres)
        elif opcion == "2": indicar_tipo(animales, nombres) 
        elif opcion == "3": indicar_tipo_por_nombre(animales, nombres)
        elif opcion == "0": break