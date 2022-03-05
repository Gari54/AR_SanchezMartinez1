#punto 1
import pandas as pd
import os
ruta = '\\Users\Gari\Desktop\Gari Jair Sanchez Martinez 1'
contenido = os.listdir(ruta)

# for archivo in contenido:
#    nombre, extension = os.path.splitext(archivo)
df= pd.DataFrame( contenido,columns=['name'])
print(df)
   #df = pd.DataFrame(contenido, columns = ['Name','Age','Percent'])