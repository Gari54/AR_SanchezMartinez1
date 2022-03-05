#punto 2
from sqlite3 import Row
from numpy import row_stack
import pandas as pd
import csv

with  open('Usuarios.csv') as File:
    r = list(File)
    dc= pd.DataFrame( r,columns=[1])
    df = pd.DataFrame(data=dc)
    print(r[' NOMBRES'], r[' APELLIDOS'], r[' DEPENDENCIA'], r[' ESTADO'], '\n')
    #for row in reader:
        #print (row)