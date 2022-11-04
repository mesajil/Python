from random import randint
from functools import reduce

def generar_matriz (N, M):
    return [[randint(0,20) for _ in range(M)] for _ in range(N)]


def imprimir(matriz):
    
    f1 = lambda a,b: f"{a}\n{b}"
    f2 = lambda a,b: f"{a}\t{b}"
    print(reduce(f1, [reduce(f2, row) for row in matriz]))
    

def guardar_matriz ():
    pass

if __name__ == "__main__":
    N = int(input("ingrese N de la Matriz: "))
    M = int(input("ingrese M de la Matriz: "))
    matriz = generar_matriz(N, M)
    imprimir(matriz)
    print("\nFin de Lectura")
    guardar_matriz (matriz)
    print(f"Guardado OK del Archivo --> matriz_{N}_por_{M}.txt")
    matriz = leer_matriz ()
    imprimir(matriz)
