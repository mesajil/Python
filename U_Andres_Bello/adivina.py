

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

        palabra_correcta = False

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

            # Salimos del bucle for

            palabra_correcta = True
            break;

        # ¿Jugador 1 perdio el juego?

        if (not palabra_correcta):
            break

        # Turno proponedor jugador 2
        
        print ("\nAhora juega Proponedor:", nombre2)

        # ...

        # ¿Jugador 2 perdio el juego?

        # ...











