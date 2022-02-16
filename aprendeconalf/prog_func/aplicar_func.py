

"""
Escribir una función que reciba otra función y una lista,
y devuelva otra lista con el resultado de aplicar la función
dada a cada uno de los elementos de la lista.
"""
import math





def aplicar_func (func, list):
    return [func(e) for e in list]



if __name__ == '__main__':
    list = [2,4,66,3,1,0]
    modificada = aplicar_func(math.factorial, list)
    print ("Lista modificada: ", modificada)
