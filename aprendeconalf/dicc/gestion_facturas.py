
"""
Escribir un programa que gestione las facturas pendientes de cobro de una empresa.
Las facturas se almacenarán en un diccionario donde la clave de cada factura será el
número de factura y el valor el coste de la factura. El programa debe preguntar al
usuario si quiere añadir una nueva factura, pagar una existente o terminar.
Si desea añadir una nueva factura se preguntará por el número de factura y su coste
y se añadirá al diccionario. Si se desea pagar una factura se preguntará por el número
de factura y se eliminará del diccionario. Después de cada operación el programa debe
mostrar por pantalla la cantidad cobrada hasta el momento y la cantidad pendiente de cobro.

Example ouput

Recaudado: 0
Pendiente de cobro:  0
¿Quieres añadir una nueva factura (A), pagarla (P) o terminar (T)?  A
Introduce el número de la factura:  1
Introduce el coste de la factura:  150
Recaudado: 0
Pendiente de cobro:  150.0
¿Quieres añadir una nueva factura (A), pagarla (P) o terminar (T)?  A
Introduce el número de la factura:  2
Introduce el coste de la factura:  300
Recaudado: 0
Pendiente de cobro:  450.0
¿Quieres añadir una nueva factura (A), pagarla (P) o terminar (T)?  P
Introduce el número de la factura a pagar:  2
Recaudado: 300.0
Pendiente de cobro:  150.0
¿Quieres añadir una nueva factura (A), pagarla (P) o terminar (T)?  A
Introduce el número de la factura:  3
Introduce el coste de la factura:  85
Recaudado: 300.0
Pendiente de cobro:  235.0
¿Quieres añadir una nueva factura (A), pagarla (P) o terminar (T)?  P
Introduce el número de la factura a pagar:  1
Recaudado: 450.0
Pendiente de cobro:  85.0
¿Quieres añadir una nueva factura (A), pagarla (P) o terminar (T)?  T

"""


def print_menu ():
    print ("Select one option:")
    print ("Add new invoice (A), pay invoice (P), show invoices (S), terminate program (T): ")


def show_data (data):
    print ()
    print ("=" * 60)
    print ("INVOICES:")
    for key, value in data[2].items():
        print(key + ": " + str(value))
    print ("Recaudado: ", data[0])
    print ("Pendiente de cobro: ", data[1])
    print ("=" * 60)

def get_new_invoice(data):
    cod = (input ("Introduce el numero de la factura: ")).upper()
    cost = float(input ("Introduce el coste de la factura: "))
    data[2][cod] = cost
    data[1] += cost


def pay_invoice (data):
    cod = input ("Introduce el numero de la factura a pagar: ").upper()
    cost = data[2][cod]
    del data[2][cod]
    data[0] += cost
    data[1] -= cost

def solve_option(opt, data):
    if (opt == "A"):
        get_new_invoice (data)
        show_data (data)
    elif (opt == "P"):
        pay_invoice (data)
        show_data (data)
    elif (opt == "S"):
        show_data (data)

def get_option ():
    opt = input ()
    return opt.upper()

if __name__ == '__main__':
    
    data = [0, 0, {}] #Definimos data como [Recaudado, pendiente, facturas]
    while (True):
        print_menu ()
        opt = get_option ()
        solve_option(opt, data)
        if opt=="T": break
