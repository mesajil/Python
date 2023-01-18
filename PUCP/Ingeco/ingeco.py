import numpy

def main():
    # KD = [0.3, 0.35, 0.45]
    # KC=[0.5]
    # D= [300_000, 250_000, 50_000]
    # C = [100_000]
    # T = 0.3
    # x = COSTO_PONDERADO_CAPITAL_DI (KD, KC, D, C, T)
    x = DEVALUACION_ACUMULADA([0.00575, 0.00286, 0.00570])
    print (x)


def PF (i, n):
    return 1/(1 + i) ** n


def FP (i, n):
    return (1 + i) ** n


def PA_UNIFORME (i, n):
    temp = (1 + i) ** n
    return (temp - 1) / (temp * i)


def PA_INFINITA (i):
    """
    Retorna P (Actualizacion de A)
    Donde:
    P: Valor presente de la serie de pagos uniforme
    A: Monto constante desembolsado en cada periodo
    i: Tasa de interes del periodo
    """
    return 1/i


def FA_UNIFORME (i, n):
    temp = (1 + i) ** n
    return (temp - 1) / i


def PG_TRIANGULO (i, n):
    temp = (1 + i) ** n
    return (temp - 1) / (temp * i ** 2) - n / (temp * i)


def PA_GEOMETRICA (i, g, n):
    if g != i:
        return (1 - ((1 + g) / (1 + i)) ** n) / (i - g)


def CALENDARIO_AMORTIZACION_CONSTANTE (P, i, n):
    SDF = P
    amortizacion = P / 15
    cuotas = []
    print("Periodo | Saldo deudor inicial | Amortizacion | Intereses | Cuota | Saldo deudor final")
    for periodo in range(n):
        intereses = SDF * i
        cuota = intereses + amortizacion
        SDI = SDF
        SDF = SDI - amortizacion
        print(f"{periodo + 1}\t{SDI:.2f}\t{amortizacion:.2f}\t{intereses:.2f}\t{cuota:.2f}\t{SDF:.2f}")
        cuotas.append(cuota)
    return cuotas


def DEVALUACION (TC_T, TC_O):
    """
    Retorna la devaluacion de la moneda desde 0 a T.
    Donde
    TC_T: Tipo de cambio al final
    TC_O: Tipo de cambio al inicio
    """
    return (TC_T - TC_O) / TC_O


def DEVALUACION_ACUMULADA (devaluaciones):
    """
    Retorna la devaluacion acumulada para una serie
    de devaluaciones.
    Donde
    devaluaciones: devaluaciones acumuladas
    """
    return numpy.prod([1 + d for d in devaluaciones]) - 1


def TASA_MONEDA_DEBIL (i, devaluacion):
    """
    Retorna la tasa de la moneda debil
    cuando la devaluacion es constante.
    Donde:
    i: Tasa de la moneda fuerte
    devaluacion: Devaluacion constante.
    """
    return (1 + i) * (1 + devaluacion) - 1


def INFLACION (IPC_T, IPC_0):
    """
    Esta funcion retorna INFLACION() utilizando los parametros: IPC_T, IPC_0
    Donde:
    INFLACION(): Es la inflacion del periodo
    IPC_T: Es el indice del precio al consumidor al final del periodo
    IPC_0: Es el indice del precio al consumidor al inicio del periodo
    """
    return (IPC_T - IPC_0)/IPC_0


def VALOR_REAL (inflacion, S):
    """
    Esta funcion deflacta el valor de S y retorna el VALOR_REAL().
    Donde:
    VALOR_REAL: Deflactacion de S
    Inflacion: Inflacion del periodo
    S: Valor corriente o nominal
    """
    return S/(1 + inflacion)


def TASA_REAL (inflacion, P, F):
    """
    Esta funcion retorna TASA_REAL() utilizando los parametros: inflacion, P y F.
    Donde:
    TASA_REAL(): Tasa de interes real del periodo
    inflacion: La inflacion del periodo
    P: Monto al inicio del periodo
    F: Monto al final del periodo
    """
    return (F/(1 + inflacion) - P)/P


def COSTO_ACCIONES_PREFERENTES (D, PC, GE):
    """
    Retorna el costo financiero esperado del financiamiento con acciones preferentes.
    Donde:
    D: Dividendo del periodo. Por ejemplo: 6% del Valor nominal
    PC: Precio de colocacion
    GE: Gastos de emision
    """
    return D / (PC - GE)


def COSTO_ACCIONES_COMUNES (D, PC, GE, g):
    """
    Retorna el costo financiero esperado del financiamiento con acciones comunes.
    Donde:
    D: Dividendo esperado del periodo.
    PC: Precio de colocacion
    GE: Gastos de emision
    g: Crecimiento esperado. Por ejemplo: 2%
    """
    return D / (PC - GE) + g


def COSTO_PONDERADO_CAPITAL_AI (K, Montos):
    """
    Retorna el costo ponderado de capital antes de Impuesto a la renta.
    Donde:
    K: Lista de tasas de costo efectivo de la deuda o de aporte propio. Por ejemplo: [30%, 35%]
    Montos: Lista de importes de financiacion con deuda o del aporte propio. Por ejemplo: [30000, 60000]
    """
    return sum([K[i] * Montos[i] for i in range(len(K))]) / sum(Montos)


def COSTO_PONDERADO_CAPITAL_DI (KD, KC, D, C, T):
    """
    Retorna el costo ponderado de capital despues de Impuesto a la renta.
    Donde:
    KD: Lista de tasas de costo efectivo de la deuda. Por ejemplo: [30%, 35%]
    KC: Lista de tasas de costo efectivo del aporte propio. Por ejemplo: [50%]
    D: Lista de importes de financiacion con deuda. Por ejemplo: [30000, 60000]
    C: Lista de importes de financiacion del aporte propio. Por ejemplo: [10000]
    T: Tasa de impuesto a la renta.
    """
    temp1 = sum([KD[i] * D[i] * (1 - T) for i in range(len(KD))]) / (sum(D) + sum(C)) 
    temp2 = sum([KC[i] * C[i] for i in range(len(KC))]) / (sum(D) + sum(C)) 
    return temp1 + temp2



if __name__ == "__main__":
    main()