from random import randint
from functools import reduce

def generar_matriz ():
    
    N = int(input("ingrese N de la Matriz: "))
    M = int(input("ingrese M de la Matriz: "))

    matriz = [[randint(0,20) for _ in range(M)] for _ in range(N)]

    imprimir(matriz)
    return matriz, N, M


def imprimir(matriz):
    print()
    print("\n".join(["\t".join([str(x) for x in row]) for row in matriz]))
    

def guardar_matriz (matriz, N, M):

    path = rf"D:\Github\Python\U\3\matriz_{N}_por_{M}.txt"
    with open(path, "w") as f:
        for r in matriz:
            f.write(",".join([str(x) for x in r]) + "\n")
    print(f"\nGuardado OK del Archivo --> matriz_{N}_por_{M}.txt")


def leer_matriz (N, M):
    print(f"\nInicio Lectura de Archivo: matriz_{N}_por_{M}.txt")
    matriz = []
    path = rf"D:\Github\Python\U\3\matriz_{N}_por_{M}.txt"
    with open(path, "r") as f:
        for x in f:
            row = [int(x) for x in x.split("\n")[0].split(",")]
            matriz.append(row)

    imprimir(matriz)
    print(f"\nFinLectura de Archivo: matriz_{N}_por_{M}.txt")

if __name__ == "__main__":
    matriz, N, M = generar_matriz()
    guardar_matriz (matriz, N, M)
    leer_matriz (N, M)
