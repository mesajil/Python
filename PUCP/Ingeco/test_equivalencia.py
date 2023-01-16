from ingeco import *
"""
Este archivo contiene los factores de equivalencia mas comunes
"""

def main():
    """
    En la funcion main se muestra un ejemplo del uso de los factores de equivalencia
    """
    # i = 0.1
    # g = 0.03
    # p1 = 3.4 * FAuniforme (i, 2) * FPsimple (i, 8)
    # p2 = 3.4 * PAgeometrica(i, g, 4) * FPsimple (i, 8)
    # p3 = 3.4 * (1 + g) ** 3 * FAuniforme (i, 4)
    # result = p1 + p2 + p3

    # i = 0.1
    # G = -400
    # g = -0.03
    # result = 10000*PAuniforme(i, 9) + G*PGtriangulo(i, 9) + (10000 +9*G) * PAgeometrica(i,g,11)*PFsimple(i, 9)
    
    i = 0.14
    K = 1000
    M = K*K
    G1 = 25*K
    G2 = 30*K
    G3 = -20*K
    g = 0.067
    I4 = 1.2*M + 3*G1
    I10 = I4 + 6*G2
    

    x = 1.2*M *PAuniforme(i, 15) + G1 * PGtriangulo(i,4) +(I4 - 1.2*M) * PAuniforme(i, 6) *PFsimple(i, 4) + G2*PGtriangulo(i, 7)*PFsimple(i, 3) + (I10 - 1.2*M) * PAuniforme(i, 5) *PFsimple(i,10) + G3 *PGtriangulo(i,6) * PFsimple(i,9)
    y = 500*K *PAuniforme(i,9) + 500*K *PAgeometrica(i,g,6)*PFsimple(i,9)
    
    print((x-y)/(1 - 0.25*0.7*PFsimple(i,15)))




if __name__ == '__main__':
    main()