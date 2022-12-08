from random import randint


# Generar matriz
N = int(input("ingrese N de la Matriz: "))
M = int(input("ingrese M de la Matriz: "))
# matriz = [[randint(0,20) for _ in range(M)] for _ in range(N)]
matriz = []
for _ in range(N):
    fila = []
    for _ in range(M):
        fila.append(randint(0,20))
    matriz.append(fila)

# Imprimir la matriz sin corchetes
print("\nLa matriz es la siguiente:\n")
# formato = "\n".join(["\t".join([str(e) for e in fila]) for fila in matriz]
formato = ""
for fila in matriz: 
    for i in range(len(fila)):
        formato += str(fila[i]) + '\t'
    formato += '\n'
print(formato)

# Guardar la matriz en un archivo externo
path = rf"matriz_{N}_por_{M}.txt"
with open(path, "w") as f:
    """Cada fila de la matriz se guarda en cada
    linea del archivo separando sus datos con comas"""
    # f.writelines([",".join([str(e) for e in fila]) + "\n" for fila in matriz])
    f.write (formato)
print(f"\nGuardado OK del Archivo ---> matriz_{N}_por_{M}.txt")

# Leer la matriz desde un archivo externo
print(f"\nInicio Lectura de Archivo: matriz_{N}_por_{M}.txt\n")
with open(path, "r") as f:
    # matriz = [line.split("\n")[0].split(",") for line in f]
    matriz = [line.replace('\n', '').split("\t") for line in f]

# Imprimir la matriz leida con formato
print("\n".join(["\t".join([str(e) for e in fila]) for fila in matriz]))
print(f"\nFin Lectura de Archivo: matriz_{N}_por_{M}.txt")

