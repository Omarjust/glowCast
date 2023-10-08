import csv
import numpy as np

# Crear un nuevo archivo CSV
with open('data_with_poisson.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(['Fecha', 'Número de eventos'])

# Importar los datos del archivo CSV
with open('prueba.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    data = list(reader)

# Calcular la media de los datos
mean = np.mean(data)

# Utilizar la función de distribución de Poisson para calcular las probabilidades
probabilities = np.array([poisson.pmf(x, mean) for x in range(max(data) + 1)])

# Agregar una columna con las probabilidades de Poisson
for row in data:
    writer.writerow([row[1], row[2], probabilities[int(row[3])]])

