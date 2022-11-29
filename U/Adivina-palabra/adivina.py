import string

def main():

    print ("BIENVENIDO AL JUEGO DE ADIVINA - PALABRA\n")
    *nombres, num_palabras, intentos = fase_configuracion ()
    puntajes = fase_proposicion_adivininacion (*nombres, num_palabras, intentos)
    fase_cierre (*nombres, *puntajes)


def fase_configuracion ():
    """Pide y retorna las variables iniciales de juego"""

    nombre1 = input("Ingrese nombre del jugador 1: ")
    nombre2 = input("Ingrese nombre del jugador 2: ")
    num_palabras = int (input ("Ingrese cantidad de palabras a adivinar por jugador: "))
    intentos = int (input ("Ingrese cantidad maxima de intentos para adivinar cada palabra: "))

    return nombre1, nombre2, num_palabras, intentos


def fase_proposicion_adivininacion (nombre1, nombre2, num_palabras, intentos):
    """Ejecuta todas las rondas de juego.
    Retorna los puntajes finales de los jugadores"""
    
    puntaje1, puntaje2 = 0, 0
    for _ in range(num_palabras):

        palabra = proponer_palabra (nombre1) # Jugador 1 es proponedor
        if (palabra == ''): # La palabra propuesta es invalida?
            return -1, 0 
        puntaje2 += adivinar_palabra (nombre2, palabra, intentos) # Jugador 2 es adivinador
        
        # Turno de jugador 2
        palabra = proponer_palabra (nombre2) # Jugador 2 es proponedor
        if (palabra == ''): # La palabra propuesta es invalida?
            return 0, -1
        puntaje1 += adivinar_palabra (nombre1, palabra, intentos) # Jugador 1 es adivinador
    
    return puntaje1, puntaje2


def proponer_palabra (nombre):
    """Retorna la palabra propuesta"""

    print ("\nAhora juega Proponedor:", nombre)

    for _ in range(3):
        palabra = input ("Ingrese palabra a adivinar: ")
        if (len(palabra) <= 20 and palabra.islower() and palabra.isalpha()):
            return palabra

    return '' # Proponedor no logra ingresar una palabra valida


def adivinar_palabra (nombre, palabra, intentos):
    """Ejecuta la etapa de adivinacion y retorna el
    puntaje obtenido por el adivinador"""

    print ("\nAhora juega Adivinador: ", nombre)

    adivinadas = set() # Letras adivinadas

    for i in range(intentos):

        letra = (input("Ingrese letra: "))[0] # Letra propuesta
        adivinadas.update(set(palabra) & set(letra)) # Agregamos letra adivinada

        # Obtenemos posiciones de "letra" en la palabra a adivinar
        posiciones = [str(i+1) for i, c in enumerate(palabra) if c == letra]
        
        # Se imprimen las posiciones encontradas 
        if (len(posiciones) > 0):
            print (f"Posiciones encontradas: {', '.join(posiciones)}")
        else:
            print ("No se encontro la letra en la palabra.")
        
        # Se retorna el puntaje
        if (set(palabra) == adivinadas):
            return round((1 - (i + 1) / intentos) * len(palabra), 2)
    
    return 0 # El adivinador no logro adivinar la palabra


def fase_cierre (nombre1, nombre2, puntaje1, puntaje2):
    """Imprime al jugador ganador y los puntajes respectivos"""

    # Jugador 1 perdio por no ingresar una palabra correctamente
    if (puntaje1 < 0):
        print ("\nGANADOR: ", nombre2)
        print (f"El jugador {nombre1} no logro ingresar una palabra correctamente.")
        return 

    # Jugador 2 perdio por no ingresar una palabra correctamente
    elif (puntaje2 < 0):
        print ("\nGANADOR: ", nombre1)
        print (f"El jugador {nombre2} no logro ingresar una palabra correctamente.")
        return

    # Jugador 1 Gano
    elif (puntaje1 > puntaje2): 
        print ("\nGANADOR: ", nombre1)

    # Jugador 2 Gano
    elif (puntaje1 < puntaje2):
        print ("\nGANADOR: ", nombre2)
    
    # Hubo empate
    else:
        print ("\nRESULTADO: EMPATE")

    # Puntajes finales
    print (f"\nPuntaje de {nombre1}: {puntaje1}")
    print (f"Puntaje de {nombre2}: {puntaje2}")


if __name__ == '__main__':
    main()
    


    








