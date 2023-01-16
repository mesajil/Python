from ingeco import *

def main():
    M = 1000000
    cuotas = CALENDARIO_AMORTIZACION_CONSTANTE (2*M * 0.8, 0.09, 15)
    print (cuotas)

    print (" + ".join([f"{cuota:.2f}*(P/F, K, {i+1})" for i,cuota in enumerate(cuotas)]))
    VP = sum([cuota*PFsimple(0.085, i+1) for i,cuota in enumerate(cuotas)])
    print (VP)
    print (2*M - VP)
    print((2*M*0.8 + 2*M*0.8*0.09)*PFsimple(0.085, 1))

if __name__ == "__main__":
    main()