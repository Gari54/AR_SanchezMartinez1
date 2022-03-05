#Punto 3
import csv
ruta_archivo = 'Usuarios.csv'

with open(ruta_archivo, newline='', encoding='utf-8') as fail:
    punto_3 = csv.DictReader(fail)
    for r in punto_3:
        print(r['CUENTA'], r[' NOMBRES'], r[' APELLIDOS'], r[' CARGO'], r[' DEPENDENCIA'], r[' OFICINA'], r[' TELEFONO'], r[' EMAIL'],r[' COMPANIA'], r[' CIUDAD'], r[' ESTADO'])

import pandas as pd

df = pd.read_csv("Usuarios.csv")

total_rows=len(df.axes[0])
total_cols=len(df.axes[1])
print("Numero de filas: "+str(total_rows))
print("Numero de columnas: "+str(total_cols))