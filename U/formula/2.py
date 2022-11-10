import pandas as pd
from matplotlib import pyplot as plt
import random
import os

random.seed(135711)


class Piloto:
    def __init__ (self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


class Equipo:
    def __init__ (self, nombre, pilotos):
        self.nombre = nombre
        self.pilotos = pilotos


class Evento:
    def __init__ (self, short_name, record_time, estimate_time, qualy_laps):
        self.short_name = short_name
        self.record_time = record_time
        self.estimate_time = estimate_time
        self.qualy_laps = qualy_laps


def leer_archivos ():
    return leer_equipos (), leer_eventos()


def leer_equipos ():
    df = pd.read_csv('equipos.csv')
    equipos = []
    competidores = int(len(df.columns.values)/2) # Numero de competidores por equipo
    for _, row in df.iterrows():
        pilotos = [] # Pilotos por equipo
        for i in range(competidores):
            nombre = row[f'piloto{i + 1}']
            edad = row[f'edad_piloto{i + 1}']
            pilotos.append(Piloto(nombre, edad))
        e = Equipo(row['nombre_equipo'], pilotos) # Creamos nuevo equipo
        equipos.append(e)
    return equipos


def leer_eventos ():
    df = pd.read_csv('tracks.csv')
    eventos = []
    for _, row in df.iterrows():
        sname = row['Short_Name']
        rtime = row['Record_Time']
        etime = row['Estimate_Time']
        ql = row['Qualy_Laps']
        eventos.append(Evento(sname, rtime, etime, ql))
    return eventos


def simular_vueltas(evento):
    vueltas = []
    for _ in range(evento.qualy_laps):
        random.seed(random.random())
        t = random.uniform(evento.estimate_time, evento.record_time)
        vueltas.append(round(t,2))
    return vueltas


def generar_csv (equipos, eventos):
    try: os.mkdir(r"resultados/")
    except FileExistsError: print ('Directory not created.')

    for ev in eventos:
        rows = []
        for eq in equipos:
            for p in eq.pilotos:
                rows.append([p.nombre, eq.nombre] + simular_vueltas(ev))
        
        path = rf"resultados/resultado_{ev.short_name}.csv"
        header = ["piloto", "equipo"] + [f"L{i + 1}" for i in range(ev.qualy_laps)]
        pd.DataFrame (rows, columns = header).to_csv(path)


def leer_tiempos (eventos):
    dicc = {}
    for ev in eventos:
        path = rf'resultados/resultado_{ev.short_name}.csv'
        df = pd.read_csv(path)
        for _, row in df.iterrows():
            if row['piloto'] not in dicc:
                dicc[row['piloto']] = [row[-1]]
            else:
                dicc[row['piloto']].append(row[-1])
    return dicc


def generar_grafico (eventos):
    dicc = leer_tiempos (eventos)
    short_names = [ev.short_name for ev in eventos]

    for nombre, resultados in dicc.items():
        plt.plot(short_names, resultados, label = nombre)

    plt.legend()
    plt.show()


if __name__ == "__main__":
    equipos, eventos = leer_archivos()
    generar_csv(equipos, eventos)
    generar_grafico(eventos)