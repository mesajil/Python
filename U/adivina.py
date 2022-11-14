import string

def fase_configuracion ():
    
    print ("BIENVENIDO AL JUEGO DE ADIVINA - PALABRA\n")

    nombre1 = input("Ingrese nombre del jugador 1: ")
    nombre2 = input("Ingrese nombre del jugador 2: ")
    num_palabras = int (input ("Ingrese cantidad de palabras a adivinar por jugador: "))
    intentos = int (input ("Ingrese cantidad maxima de intentos para adivinar cada palabra: "))

    return nombre1, nombre2, num_palabras, intentos


def fase_proposicion_adivininacion (nombre1, nombre2, num_palabras, intentos):

    puntaje1, puntaje2 = 0, 0
    for _ in range(num_palabras):
        # Turno de jugador 1
        palabra = proponer_palabra (nombre1)
        if (palabra == ''): return -1, 0
        puntaje2 += adivinar_palabra (nombre2, palabra, intentos)
        
        # Turno de jugador 2
        palabra = proponer_palabra (nombre2)
        if (palabra == ''): return 0, -1
        puntaje1 += adivinar_palabra (nombre1, palabra, intentos)
    
    return puntaje1, puntaje2


def proponer_palabra (nombre):

    print ("\nAhora juega Proponedor:", nombre)

    for _ in range(3):

        palabra = input ("Ingrese palabra a adivinar: ")
        if (len(palabra) > 20): continue
        if (any(c not in string.ascii_lowercase for c in palabra)): continue
        return palabra

    return ''


def adivinar_palabra (nombre, palabra, intentos):

    print ("\nAhora juega Adivinador: ", nombre)

    adivinadas = set()

    for i in range(intentos):

        letra = (input("Ingrese letra: "))[0]
        adivinadas.update(set(palabra) & set(letra))
        posiciones = [str(j + 1) for j in range(len(palabra)) if letra == palabra[j]]
        
        if (len(posiciones) > 0):
            print (f"Posiciones encontradas: {', '.join(posiciones)}")
        else:
            print ("No se encontro la letra en la palabra.")
        
        if (set(palabra) == adivinadas):
            return (1 - (i + 1) / intentos) * len(palabra)
    
    return 0


def fase_cierre (nombre1, nombre2, puntaje1, puntaje2):

    print ()
    if (puntaje1 < 0):
        print ("GANADOR: ", nombre2)
        print (f"El jugador {nombre1} no logro ingresar una palabra correctamente.")
        return 
    elif (puntaje2 < 0):
        print ("GANADOR: ", nombre1)
        print (f"El jugador {nombre2} no logro ingresar una palabra correctamente.")
        return
    elif (puntaje1 > puntaje2):
        print ("GANADOR: ", nombre1)
    elif (puntaje1 < puntaje2):
        print ("GANADOR: ", nombre2)
    else:
        print ("EMPATE")

    print (f"\nPuntaje de {nombre1}: {round(puntaje1,2)}")
    print (f"Puntaje de {nombre2}: {round(puntaje2,2)}")


def main():

    data = fase_configuracion ()
    puntaje1, puntaje2 = fase_proposicion_adivininacion (*data)
    nombre1, nombre2, _, _ = data
    fase_cierre (nombre1, nombre2, puntaje1, puntaje2)


if __name__ == '__main__':
    main()
    


    








