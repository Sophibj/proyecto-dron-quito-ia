# -*- coding: utf-8 -*-
"""
ECD IA
Generación de dataset simulado para sistema de drones en Quito
"""

import pandas as pd
import numpy as np
import os
import datetime as dt

np.random.seed(42)

# Crear carpeta si no existe
os.makedirs("data/simulated", exist_ok=True)

n = 800

rutas = np.random.choice(["RUTA_A","RUTA_B","RUTA_C"], size=n)

clima = np.random.choice(
    ["SOLEADO","NUBLADO","LLUVIA","LLUVIA_FUERTE"],
    size=n,
    p=[0.35,0.30,0.25,0.10]
)

viento = np.random.choice(
    ["BAJO","MEDIO","ALTO","MUY_ALTO"],
    size=n,
    p=[0.35,0.35,0.20,0.10]
)

temperatura = np.random.normal(16,4,n).clip(2,28)

peso = np.random.uniform(0.5,40,n)

dim_l = np.random.randint(10,80,n)
dim_a = np.random.randint(10,80,n)
dim_h = np.random.randint(5,60,n)

bateria_inicio = np.random.randint(80,100,n)

distancia = np.random.uniform(1,18,n)

obstaculos = np.random.binomial(1,0.18,n)
trafico = np.random.binomial(1,0.12,n)

# simulación de consumo de batería
consumo = distancia * 2 + obstaculos * 5 + trafico * 3
bateria_fin = bateria_inicio - consumo
bateria_fin = bateria_fin.clip(0,100)

# resultado entrega
resultado = []

for i in range(n):

    if clima[i] == "LLUVIA_FUERTE":
        resultado.append(0)

    elif viento[i] == "MUY_ALTO":
        resultado.append(0)

    elif bateria_fin[i] < 20:
        resultado.append(0)

    else:
        resultado.append(1)

base = dt.datetime(2026,1,1,6,0,0)

salida = []
llegada = []

for i in range(n):

    t = base + dt.timedelta(minutes=int(np.random.uniform(0,720)))
    salida.append(t)

    llegada.append(t + dt.timedelta(minutes=float(np.random.uniform(5,30))))

df = pd.DataFrame({

"id_vuelo":[f"V{i}" for i in range(n)],

"ruta":rutas,

"distancia_km":distancia,

"peso_kg":peso,

"dim_l_cm":dim_l,
"dim_a_cm":dim_a,
"dim_h_cm":dim_h,

"bateria_inicio":bateria_inicio,
"bateria_fin":bateria_fin,

"clima":clima,

"viento":viento,

"temperatura":temperatura,

"obstaculos":obstaculos,
"trafico_aereo":trafico,

"fecha_salida":salida,
"fecha_llegada":llegada,

"resultado_entrega":resultado

})

path = "data/simulated/dataset_drone_quito.csv"

df.to_csv(path,index=False)

print("Dataset generado en:", path)

print(df.head())