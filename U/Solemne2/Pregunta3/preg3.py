from random import randint

def main():

    N = int(input("ingrese N de la Matriz: "))
    M = int(input("ingrese M de la Matriz: "))

    matriz = [[randint(0,20) for _ in range(M)] for _ in range(N)]
    
    imprimir_matriz(matriz)
    guardar_matriz (matriz, N, M)
    leer_matriz (N, M)


def imprimir_matriz(matriz):
    """Imprime la matriz con formato"""

    print("\nLa matriz es la siguiente:\n")
    print("\n".join(["\t".join([str(e) for e in row]) for row in matriz]))
    

def guardar_matriz (matriz, N, M):
    """Guarda la matriz en un archivo externo"""
    
    path = rf"matriz_{N}_por_{M}.txt"
    with open(path, "w") as f:
        """Cada fila de la matriz se guarda en cada
        linea del archivo"""
        f.writelines([",".join([str(e) for e in row]) + "\n" for row in matriz])
    print(f"\nGuardado OK del Archivo ---> matriz_{N}_por_{M}.txt")


def leer_matriz (N, M):
    """Lee la matriz desde un archivo externo"""

    print(f"\nInicio Lectura de Archivo: matriz_{N}_por_{M}.txt")
    
    path = rf"matriz_{N}_por_{M}.txt"
    with open(path, "r") as f:
        matriz = [line.split("\n")[0].split(",") for line in f]

    imprimir_matriz(matriz)
    print(f"\nFin Lectura de Archivo: matriz_{N}_por_{M}.txt")


if __name__ == "__main__":
    main()