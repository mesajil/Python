from random import randint

def main():

    # Definir matriz
    N = int(input("ingrese N de la Matriz: "))
    M = int(input("ingrese M de la Matriz: "))
    matriz = [[randint(0,20) for _ in range(M)] for _ in range(N)]

    # Imprimir la matriz sin corchetes
    print("\nLa matriz es la siguiente:\n")    
    # print("\n".join(["\t".join([str(e) for e in row]) for row in matriz])) # Utilizando list comprehension
    # for row in matriz: # Utilizando condicionales
    #     for i in range(len(row)):
    #         if i < len(row) - 1:
    #             print(row[i], end='\t')
    #         else:
    #             print(row[i])

    for row in matriz: # Utilizando join
        print("\t".join([str(e) for e in row]))

    # Guardar la matriz en un archivo externo
    path = rf"matriz_{N}_por_{M}.txt"
    with open(path, "w") as f:
        """Cada fila de la matriz se guarda en cada
        linea del archivo separando sus datos con comas"""
        f.writelines([",".join([str(e) for e in row]) + "\n" for row in matriz])
    print(f"\nGuardado OK del Archivo ---> matriz_{N}_por_{M}.txt")

    # Leer la matriz desde un archivo externo
    print(f"\nInicio Lectura de Archivo: matriz_{N}_por_{M}.txt\n")
    with open(path, "r") as f:
        matriz = [line.split("\n")[0].split(",") for line in f]
    
    # Imprimir la matriz leida con formato
    print("\n".join(["\t".join([str(e) for e in row]) for row in matriz]))
    print(f"\nFin Lectura de Archivo: matriz_{N}_por_{M}.txt")


if __name__ == "__main__":
    main()