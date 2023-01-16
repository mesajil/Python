def PF (i, n):
    return 1/(1 + i) ** n


def FP (i, n):
    return (1 + i) ** n


def PA_UNIFORME (i, n):
    temp = (1 + i) ** n
    return (temp - 1) / (temp * i)


def PA_INFINITA (i):
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
    F: onto al final del periodo
    """
    return (F/(1 + inflacion) - P)/P

