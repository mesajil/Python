"""
La pizzería Bella Napoli ofrece pizzas vegetarianas y no
vegetarianas a sus clientes. Los ingredientes para cada tipo
de pizza aparecen a continuación.

Ingredientes vegetarianos: Pimiento y tofu.
Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

Escribir un programa que pregunte al usuario si quiere
una pizza vegetariana o no, y en función de su respuesta
le muestre un menú con los ingredientes disponibles para
que elija. Solo se puede eligir un ingrediente además de
la mozzarella y el tomate que están en todas la pizzas.

Al final se debe mostrar por pantalla si la pizza elegida
es vegetariana o no y todos los ingredientes que lleva.
"""



def get_pizza ():
    str_is_veg_pizza = input("¿Desea pizza vegetariana? y/n: ")
    return True if str_is_veg_pizza == "y" else False


def get_ingredient (is_veg_pizza):
    
    veg_ingridients = ["Pimiento", "tofu"]
    no_veg_ingridients = ["Peperoni", "Jamon", "Salmon"]
    txt_options = ["Peperoni(1), Jamon(2) y Salmon(3): ", "Pimiento(1) y tofu(2): "]

    print ("Please, select one ingredient from this list: ")
    option = int (input (txt_options[int(is_veg_pizza)]))

    if is_veg_pizza:
        ingredient = veg_ingridients[option - 1]
    else:
        ingredient = no_veg_ingridients[option - 1]
    return ingredient


def print_order (is_veg_pizza, ingredient):
    print()
    line = "=" * 60
    print (line)
    print ("\tThank you!, your order is being prepared.")
    print ("\tVegetable pizza: ", "YES" if is_veg_pizza else "NO")
    print ("\tIgridients: Mozzarella, tomate and ", ingredient)
    print (line)








if __name__ == '__main__':
    is_veg_pizza = get_pizza ()
    ingredient = get_ingredient (is_veg_pizza)
    print_order (is_veg_pizza, ingredient)
