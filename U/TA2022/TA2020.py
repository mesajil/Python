def main():
    menu = """
    MENU

    [1] Conversion de binario a decimal
    [2] Evaluar numeros
    [3] Codificacion de alumno
    [4] Juego de preguntas
    [5] Juego de numeros
    [6] Salir

    Ingrese la opcion: """

    while True:
        opcion = input(menu)
        match opcion:
            case "1": conversion_binariodecimal ()
            case "2": evaluar_numeros()
            case "3": codificacion_alumno()
            case "4": juego_preguntas()
            case "5": juego_numeros()
            case "6": break


def conversion_binariodecimal ():
    binario = int(input("Ingrese numero binario: "))
    decimal, i = 0, 0
    while(binario != 0):
        digito = binario % 10 # Ultimo digito de binario
        decimal += digito * pow(2, i)
        binario //= 10 # Quitar ultimo digito a binario
        i += 1
    print("Decimal:", decimal)


def evaluar_numeros ():
    cantidad = int(input("Cantidad de numeros a evaluar: "))
    lista = [] # Lista de numeros a evaluar
    i = 0 # Contador
    while (i < cantidad):
        numero = int(input(f"Ingrese numero {i + 1}: "))
        numero = str(numero) # La lista sera una lista de strings
        if numero not in lista:
            lista.append(numero) # Se agrega numero a la lista 
            i += 1 # Incrementar contador
        else:
            print("El numero es repetido, ingrese otro nuevamente.")
    print ("Numeros:", ', '.join(lista))


def codificacion_alumno ():
    print ("Codificacion del alumno:\n")
    nombre = input("Ingrese nombre: ").upper() # Se guarda en mayusculas
    paterno = input("Ingrese apellido paterno: ").upper() # Se guarda en mayusculas
    materno = input("Ingrese apellido materno: ").upper() # Se guarda en mayusculas
    fecha = input("Ingrese fecha de nacimiento (formato dd/mm/aaaa): ")
    genero = input("Ingrese genero (1=hombre, 2=mujer): ")
    titular = input("Ingrese una opcion (1=titular, 2=dependiente): ")
    dd, mm, aaaa = fecha.split('/')
    codigo = aaaa + mm + dd + genero[0] # genero debe ser "1" o "2"
    codigo += paterno[0] + (paterno[3] if len(paterno) >= 4 else paterno[-1])
    codigo += materno[0] + (materno[3] if len(materno) >= 4 else materno[-1])
    codigo += nombre[0] + ("001" if titular[0] == "1" else "002")
    print("Codigo de seguro:", codigo)


def juego_preguntas():
    pass


def juego_numeros ():
    pass


main()