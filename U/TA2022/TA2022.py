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
    class Pregunta:
        def __init__ (self, pregunta, alternativas, respuesta):
            self.pregunta = pregunta
            self.alternativas = alternativas # Lista con las alternativas
            self.respuesta = respuesta # Indice de la lista de alternativas

        def obtener_respuesta(self):
            # Devuelve el elemento de la lista correcto
            return self.alternativas[self.respuesta - 1]
    
    print ("Juego de preguntas")
    preguntas = [] # Lista de objetos Pregunta()
    preguntas.append(Pregunta(
        "Cuantos litros de sangre tiene una persona adulta?",
        ["Tiene entre 2 y 4 litros", "Tiene entre 4 y 6 litros"],
        2
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
    
    print ("\nResultados:")
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

    input("\nPresione enter para continuar.")


def juego_numeros ():
    pass


main()