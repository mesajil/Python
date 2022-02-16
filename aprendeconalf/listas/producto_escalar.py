

"""
#11

Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2)
en dos listas y muestre por pantalla su producto escalar.
"""


import numpy as np



def get_vector (long):
    vector = []
    print ("Please, enter the "+str(long)+" values of the vector.")
    for i in range(long):
        vector.append (float (input("New value: ")))


#def producto_escalar(vector_1, vector_2):
    






if __name__ == '__main__':
    long = 3
    vector_1 = get_vector(long)
    vector_2 = get_vector(long)
    producto_escalar = producto_escalar(vector_1, vector_2)
    print_product(producto_escalar)
