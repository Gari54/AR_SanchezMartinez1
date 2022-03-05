
import os
ruta = '\\Users\Gari\Desktop\Gari Jair Sanchez Martinez 1'
contenido = os.listdir(ruta)

for archivo in contenido:
    nombre, extension = os.path.splitext(archivo)
    print("{}' nombre '{}' extensión '{}' ruta: '{}'".format(archivo, nombre, extension ,ruta))
    print()

import csv

with  open('Usuarios.csv') as File:
    reader = list(File)
    for row in reader:
        print (row)

ruta_archivo = 'Usuarios.csv'

with open(ruta_archivo, newline='', encoding='utf-8') as fail:
    punto_3 = csv.DictReader(fail)
    for r in punto_3:
        print(r[' NOMBRES']; r[' APELLIDOS']; r[' DEPENDENCIA']; r[' ESTADO']; '\n' )

import pandas as pd

df = pd.read_csv("Usuarios.csv")

total_rows=len(df.axes[0])
total_cols=len(df.axes[1])
print("Numero de filas: "+str(total_rows))
print("Numero de columnas: "+str(total_cols))