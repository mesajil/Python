from os import system

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
        system('clear') # Limpia la pantalla
        opcion = input(menu)
        system('clear') # Limpia la pantalla
        match opcion:
            case "1": conversion_binariodecimal ()
            case "2": evaluar_numeros()
            case "3": codificacion_alumno()
            case "4": juego_preguntas()
            case "5": juego_numeros()
            case "6": break
            case _: continue
        input("\nPresione enter para continuar.")


def conversion_binariodecimal ():
    binario = int(input("Ingrese numero binario: "))
    decimal = 0 # Inicialmente en 0
    i = 0 # Exponente
    while(binario != 0):
        digito = binario % 10 # Ultimo digito del numero binario
        decimal += digito * pow(2, i) # Incrementa decimal
        binario //= 10 # Quitar ultimo digito al numero binario
        i += 1 # Incrementa exponente
    print("Decimal:", decimal)


def evaluar_numeros ():
    cantidad = int(input("Cantidad de numeros a evaluar: "))
    lista = [] # Lista de numeros a evaluar
    i = 0 # Contador
    while (i < cantidad):
        numero = int(input(f"Ingrese numero {i + 1}: "))
        numero = str(numero) # Los numeros son strings
        if numero not in lista:
            lista.append(numero) # Se agrega numero a la lista 
            i += 1 # Incrementar contador
        else:
            print("El numero es repetido, ingrese otro nuevamente.")
    print ("Numeros:", ', '.join(lista)) # Los numeros se separan por comas


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
    print("\nCodigo de seguro:", codigo)


def juego_preguntas():
    class Pregunta:
        def __init__ (self, pregunta, alternativas, respuesta):
            self.pregunta = pregunta
            self.alternativas = alternativas # Lista con las alternativas
            self.respuesta = respuesta # Indice correcto de la lista de alternativas

        def obtener_respuesta(self):
            # Devuelve la respuesta correcta
            return self.alternativas[self.respuesta - 1]
    
    print ("Juego de preguntas")
    preguntas = [] # Lista de objetos Pregunta()
    preguntas.append(Pregunta(
        "Cuantos litros de sangre tiene una persona adulta?", # Pregunta
        ["Tiene entre 2 y 4 litros", "Tiene entre 4 y 6 litros"], # Lista de alternativas
        2 # Indice de la respuesta correcta
    ))
    preguntas.append(Pregunta(
        "Quien es el autor de la frase \"Pienso, luego existo\"?",
        ["Descartes", "Socrates"],
        1
    ))
    preguntas.append(Pregunta(
        "Cual es el pais mas grande y el mas pequeno del mundo?",
        ["China y Nauru", "Rusia y Vaticano"],
        2
    ))
    preguntas.append(Pregunta(
        "Cual es el libro mas vendido en el mundo despues de la Biblia?",
        ["Don Quijote de la Mancha", "La Odisea"],
        1
    ))
    preguntas.append(Pregunta(
        "La sal comun esta formada por dos elementos, cuales son?",
        ["Sodio y carbono", "Sodio y cloro"],
        2
    ))
    preguntas.append(Pregunta(
        "Quien pinto la obra \"Guernica\"?",
        ["Salvador Dali", "Pablo Picasso"],
        2
    ))
    preguntas.append(Pregunta(
        "Cuanto tiempo tarda la luz del Sol en llegar a la Tierra?",
        ["12 horas", "8 minutos"],
        2
    ))
    preguntas.append(Pregunta(
        "Cual es la nacionalidad de Jorge Mario Bergoglio?",
        ["Mexicana", "Argentina"],
        2
    ))
    preguntas.append(Pregunta(
        "En que periodo de la prehistoria fue descubierto el fuego?",
        ["Neolitico", "Paleolitico"],
        2
    ))
    preguntas.append(Pregunta(
        "A quien se le atribuye la frase \"Solo se que no se nada\"?",
        ["Socrates", "Aristoteles"],
        1
    ))

    puntaje = 0 # Puntaje del jugador
    for i,p in enumerate(preguntas):
        print (f"\n{i + 1}. {p.pregunta}")
        print (f"1. {p.alternativas[0]}") # Primera alternativa
        print (f"2. {p.alternativas[1]}") # Segunda alternativa
        opcion = int(input("Elegir alternativa: "))
        if opcion == p.respuesta:
            print("Correcto!")
            puntaje += 1
        else:
            print(f"Incorrecto, la respuesta correcta es: {p.obtener_respuesta()}")
    
    print ("\nResultados\n")
    print (f"Correctas:     {puntaje}")
    print (f"Incorrectas:   {len(preguntas) - puntaje}")
    
    if puntaje <= 4:
        print ("Nivel Alcanzado: Deficiente")
    elif puntaje == 5:
        print ("Nivel Alcanzado: Regular")
    elif puntaje <= 8:
        print ("Nivel Alcanzado: Bueno")
    else:
        print ("Nivel Alcanzado: Excelente")


def juego_numeros ():
    from random import randint
    print("Juego de numeros\n")
    apuesta = int(input("Ingrese su monto de apuesta: "))
    lista = [] # Lista de numeros del usuario
    i = 0 # Contador
    while (i < 3):
        numero = int(input(f"Ingrese numero {i + 1}: "))
        if numero not in range(1,7): # Verifica que numero no este entre 1 y 6
            print("El numero debe estar entre 1 y 6.")
        elif numero not in lista:
            lista.append(numero) # Se agrega numero a la lista 
            i += 1 # Incrementar contador
        else:
            print("El numero es repetido, ingrese otro nuevamente.")

    generados = [randint(1,6) for _ in range(3)] # Generar lista de numeros random entre 1 y 6
    aciertos = 0
    for numero in lista:
        if numero in generados:
            aciertos += 1
    print ("\nResultados\n")
    print ("Tus numeros:        ", lista)
    print ("Numeros generados:  ", generados)
    print ("Aciertos:                   ", aciertos)
    match aciertos:
        case 0:
            print ("Pierdes tu apuesta:         ",0)
        case 1:
            print ("Conservas tu apuesta:       ", apuesta)
        case 2:
            print ("Multiplicas tu apuesta (x2):", apuesta*2)
        case 3:
            print ("Multiplicas tu apuesta (x3):", apuesta*3)


main()