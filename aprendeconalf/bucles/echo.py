"""
#13

Escribir un programa que muestre el eco de todo lo
que el usuario introduzca hasta que el usuario escriba
“salir” que terminará.
"""



def echo ():
    while (True):
        word = input ("Ingrese palabra: ")
        if word == "salir":
            print ("Fin del programa")
            break
        print (word)




if __name__ == '__main__':
    echo()

