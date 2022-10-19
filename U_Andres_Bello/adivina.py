def fase_configuracion ():
    
    nombre1 = input("Ingrese nombre del jugador 1: ")
    nombre2 = input("Ingrese nombre del jugador 2: ")
    num_palabras = int (input ("Ingrese cantidad de palabras a adivinar por jugador: "))
    max_intentos = int (input ("Ingrese cantidad maxima de intentos para adivinar cada palabra: "))

    return nombre1, nombre2, num_palabras, max_intentos

def fase_proposicion_adivininacion (nombre1, nombre2, num_palabras, max_intentos):

    for _ in range(num_palabras):

        palabra = proponer_palabra (nombre1)
        puntaje2 = adivinar_palabra (nombre2, palabra, max_intentos)
        palabra = proponer_palabra (nombre2)
        puntaje1 = adivinar_palabra (nombre1, palabra, max_intentos)
    
    return puntaje1, puntaje2


def proponer_palabra (nombre):

    print ("\nAhora juega Proponedor:", nombre)

    for _ in range(3):
        palabra = input ("Ingrese palabra a adivinar: ")

        # Verificamos que el tamaño de la palabra sea menor o igual a 20

        if (len(palabra) > 20):
            continue

        # Verificamos que cada carácter en la cadena sea minúscula y pertenezca al alfabeto español.

        palabra_esp = True
        
        for caracter in palabra:
            if caracter not in "abcdefghijklmnñopqrstuvwxyz":
                palabra_esp = False
                break
        
        if (not palabra_esp):
            continue 

        # Se retorna la palabra

        return palabra

    # No se ingreso una palabra correctamente

    return 0


def adivinar_palabra (nombre, palabra, max_intentos):

    print ("\nAhora juega Adivinador: ", nombre)

    letras_a_adivinar = set(palabra)
    letras_adivinadas = set()

    for i in range(max_intentos):

        letra = (input("Ingrese letra: "))[0]

        # Mostrar posiciones

        if (letra in palabra):
            letras_adivinadas.update(letra)
            posiciones = []
            for p in range(len(palabra)):
                if (letra == palabra[p]):
                    posiciones.append(str(p + 1))

            print ("La letra se encontro en las posiciones: " + ", ".join(posiciones))
        else:
            print ("No se encontro la letra en la palabra a adivinar.")
        
        # Retornar puntaje

        if (len(letras_a_adivinar) == len(letras_adivinadas)):
            return (1 - (i + 1) / max_intentos) * len(palabra)
    
    return 0

def fase_cierre (puntaje1, puntaje2):

    if (puntaje1 < 0):
        pass


if __name__ == '__main__':

    print ("BIENVENIDO AL JUEGO DE ADIVINA - PALABRA\n")
    nombre1, nombre2, num_palabras, max_intentos = fase_configuracion ()
    puntaje1, puntaje2 = fase_proposicion_adivininacion (nombre1, nombre2, num_palabras, max_intentos)
    fase_cierre (puntaje1, puntaje2)
    

    








