import pandas as pd
from matplotlib import pyplot as plt
import random

def Piloto:
    def __init__ (self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


def Equipo:
    def __init__ (self, nombre, pilotos):
        self.nombre = nombre
        self.pilotos = pilotos


def Eventos:
    def __init__ (self, short_name, record_time, estimate_time, qualy_laps):
        self.short_name = short_name
        self.record_time = record_time
        self.estimate_time = estimate_time
        self.qualy_laps = qualy_laps


def leer_archivos ():
    tracks = pd.read_csv('tracks.csv')
    equipos = pd.read_csv('equipos.csv')
    return tracks, equipos


def crear_equipos (dfequipos):
    equipos = []
    competidores = int(len(dfequipos.columns.values)/2) # Numero de competidores por equipo
    for _, row in dfequipos.iterrows():
        pilotos = [] # Pilotos por equipo
        for i in range(competidores):
            nombre = row[f'piloto{i + 1}']
            edad = row[f'edad_piloto{i + 1}']
            pilotos.append(Piloto(nombre, edad))
        e = Equipo(row['nombre_equipo'], pilotos) # Creamos nuevo equipo
        equipos.append(e)
    return equipos


def leer_eventos (dftracks):
    eventos = []
    for _, row in dftracks.iterrows():
        sname = row['Short_Name']
        rtime = row['Record_Time']
        etime = row['Estimate_Time']
        ql = row['Qualy_Laps']
        eventos.append(Evento(sname, rtime, etime, ql))
    return eventos


def generar_csv (equipos, eventos):
    for ev in eventos:
        rows = [] # 
        for eq in equipos:
            for p in eq:
                rows.append([p.nombre, eq.nombre] + p.resultados[ev.short_name])
        
        header = ["piloto", "equipo"] + [f"L{i + 1}" for i in range(ev.qualy_laps)]
        path = f"resultado_{ev.short_name}.csv"
        pd.DataFrame (data, columns = header).to_csv(path)



if __name__ == "__main__":
    dftracks, dfequipos = leer_archivos()
    equipos = leer_equipos (dfequipos)
    eventos = leer_eventos (dftracks)
    generar_csv(equipos, eventos)