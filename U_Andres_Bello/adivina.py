def obtener_palabra_a_adivinar ():

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


def adivinar_palabra (palabra, max_intentos):

    letras_unicas = set(palabra)
    letras_encontradas = set()

    for i in range(max_intentos):

        letra = (input("Ingrese letra: "))[0]

        # Econtrar posiciones de letra en palabra

        if (letra in palabra):
            posiciones = encontrar_posiciones(letra, palabra)
        
        # Retornar puntaje si se adivinó la palabra

        if (len(letras_encontradas) == len(letras_unicas)):
            # Retorna puntaje
    
    return 0

if __name__ == '__main__':
    
    # Fase de configuración

    print ("BIENVENIDO AL JUEGO DE ADIVINA - PALABRA\n")
    nombre1 = input("Ingrese nombre del jugador 1: ")
    nombre2 = input("Ingrese nombre del jugador 2: ")
    num_palabras = int (input ("Ingrese cantidad de palabras a adivinar por jugador: "))
    max_intentos = int (input ("Ingrese cantidad máxima de intentos para adivinar cada palabra: "))

    # Fase de Proposición-Adivinación

    for _ in range(num_palabras):
        
        # Turno proponedor jugador 1
        
        print ("\nAhora juega Proponedor:", nombre1)

        palabra = obtener_palabra_a_adivinar()

        # ¿Jugador 1 perdio el juego?

        if (palabra == 0):
            break

        # Turno adivinador jugador 2

        print ("\nAhora juega Adivinador:", nombre2)

        # Turno proponedor jugador 2
        
        print ("\nAhora juega Proponedor:", nombre2)

        palabra = obtener_palabra_a_adivinar()

        # ¿Jugador 2 perdio el juego?

        if (palabra == 0):
            break

        # Turno adivinador jugador 2

        print ("\nAhora juega Adivinador:", nombre1)

    

    








