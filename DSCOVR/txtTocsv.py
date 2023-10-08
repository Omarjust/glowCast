import csv

# Nombre del archivo de entrada y salida
archivo_txt = "enBruto.txt"
archivo_csv = "valores.csv"

# Abre el archivo TXT para lectura y el archivo CSV para escritura
with open(archivo_txt, 'r') as entrada, open(archivo_csv, 'w', newline='') as salida:
    # Crea un objeto escritor CSV
    escritor_csv = csv.writer(salida)
    
    # Itera sobre las líneas del archivo TXT
    for linea in entrada:
        # Divide la línea en columnas usando espacios o tabulaciones como separadores
        columnas = linea.strip().split()  # Puedes usar '\t' en lugar de ' ' si es necesario
        
        # Escribe las columnas en el archivo CSV
        escritor_csv.writerow(columnas)

print(f"Archivo CSV '{archivo_csv}' creado con éxito.")

