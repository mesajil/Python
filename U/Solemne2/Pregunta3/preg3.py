from random import randint

def generar_matriz ():
    
    N = int(input("ingrese N de la Matriz: "))
    M = int(input("ingrese M de la Matriz: "))

    return [[randint(0,20) for _ in range(M)] for _ in range(N)], N, M


def imprimir_matriz(matriz):
    
    print("\nLa matriz es la siguiente:\n")
    print("\n".join(["\t".join([str(x) for x in row]) for row in matriz]))
    

def guardar_matriz (matriz):
    
    N = len(matriz)
    M = len(matriz[0])
    
    path = rf"matriz_{N}_por_{M}.txt"
    with open(path, "w") as f:
        f.writelines([",".join([str(x) for x in row]) + "\n" for row in matriz])
    print(f"\nGuardado OK del Archivo ---> matriz_{N}_por_{M}.txt")


def leer_matriz (N, M):
    print(f"\nInicio Lectura de Archivo: matriz_{N}_por_{M}.txt")
    
    path = rf"matriz_{N}_por_{M}.txt"
    with open(path, "r") as f:
        matriz = [line.split("\n")[0].split(",") for line in f]

    imprimir_matriz(matriz)
    print(f"\nFin Lectura de Archivo: matriz_{N}_por_{M}.txt")


def main():
    matriz, N, M = generar_matriz()
    imprimir_matriz(matriz)
    guardar_matriz (matriz)
    leer_matriz (N, M)


if __name__ == "__main__":
    main()