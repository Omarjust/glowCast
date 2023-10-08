import pandas as pd

# Cargar el archivo csv
df = pd.read_csv('valoresCorrectos.csv')

# Seleccionar solo las columnas 0, 1, 21, 24 y 27
df = df.iloc[:, [0, 1, 21, 24, 27]]

# Guardar el dataframe en un nuevo archivo csv
df.to_csv('datosSeleccionados.csv', index=False)

