"""
Este archivo contiene los factores de equivalencia mas comunes
"""

def main():
    """
    En la funcion main se muestra un ejemplo del uso de los factores de equivalencia
    """
    i = 0.1
    g = 0.03
    p1 = 3.4 * FAuniforme (i, 2) * FPsimple (i, 8)
    p2 = 3.4 * PAgeometrica(i, g, 4) * FPsimple (i, 8)
    p3 = 3.4 * (1 + g) ** 3 * FAuniforme (i, 4)
    result = p1 + p2 + p3
    print(result)


def PFsimple (i, n):
    return 1/(1 + i) ** n


def FPsimple (i, n):
    return (1 + i) ** n


def PAuniforme (i, n):
    temp = (1 + i) ** n
    return (temp - 1) / (temp * i)


def PAinfinita (i):
    return 1/i


def FAuniforme (i, n):
    temp = (1 + i) ** n
    return (temp - 1) / i


def PGtriangulo (i, n):
    temp = (1 + i) ** n
    return (temp - 1) / (temp * i ** 2) - n / (temp * i)


def valorPresenteGlineal (A, G, i, n):
    return A * PAuniforme(i, n) + G * PGtriangulo(i, n)


def PAgeometrica (i, g, n):
    if g != i:
        temp1 = (1 + i) ** n
        temp2 = (1 + g) ** n
        return (1 - temp2 / temp1) / (i - g)


if __name__ == '__main__':
    main()