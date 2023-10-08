import pandas as pd

# Cargar el archivo csv
df = pd.read_csv('datosSeleccionados.csv')

# Seleccionar solo las columnas 0, 1, 4
df = df.iloc[:, [0, 1, 4]]

# Guardar el dataframe en un nuevo archivo csv
df.to_csv('valores/temperatura.csv', index=False)
