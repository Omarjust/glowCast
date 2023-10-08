import pandas as pd

# Carga tu archivo csv ignorando las primeras 13 filas
df = pd.read_csv('valores.csv', skiprows=13)

# Obtiene el nombre de la cuarta columna
columna1 = df.columns[22]
columna2 = df.columns[2]

# Elimina las filas donde la cuarta columna es menor a 0
df = df[df[columna1] > 0]
df = df[df[columna2] > 0]

# Guarda el dataframe resultante en un nuevo archivo csv
df.to_csv('valoresCorrectos.csv', index=True)

