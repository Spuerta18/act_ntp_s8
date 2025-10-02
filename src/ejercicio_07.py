import csv
import pandas as pd

def leer_csv_cursos():
    nombre_archivo = "cursos.csv"
    
   
    cursos = [
        ['curso', 'instructor', 'duracion'],
        ['Python Básico', 'Ana Pérez', '20 horas'],
        ['Pandas Avanzado', 'Luis Gómez', '15 horas'],
        ['Machine Learning', 'María López', '25 horas']
    ]
    
    # Escribir datos en el archivo CSV
    with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerows(cursos)
    
    # Intentar leer el archivo con pandas
    try:
        df = pd.read_csv(nombre_archivo)
        print("DataFrame leído desde el archivo CSV:")
        print(df)
    except FileNotFoundError:
        print(f"Error: el archivo '{nombre_archivo}' no existe.")


leer_csv_cursos()
