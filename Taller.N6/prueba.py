from email import header
import os
from numpy import column_stack, row_stack
import tabulate
import pandas as pd

with  open('Usuarios.csv') as File:
    r = object(File)
    c =column_stack(r)
    nombre, extension = os.path.splitext(r)
    print("nombre '{}' extensión '{}'".format(nombre, extension ,))
    #df = pd.DataFrame(data=r)
    #print(c[0])