"""
#13

Escribir un programa que muestre el eco de todo lo
que el usuario introduzca hasta que el usuario escriba
“salir” que terminará.
"""



def solve ():
    word = ""
    while (word != "salir"):
        word = input ("Ingrese palabra: ")
        if (word != "salir"):
            print (word)
    print ("Fin del programa")



if __name__ == '__main__':
    solve()

