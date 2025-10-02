import json
import pandas as pd

def leer_json_vehiculos():
    nombre_archivo = "vehiculos.json"
    
    # Lista de objetos (vehículos)
    vehiculos = [
        {"marca": "Toyota", "modelo": "Corolla", "año": 2020},
        {"marca": "Ford", "modelo": "Focus", "año": 2018},
        {"marca": "Honda", "modelo": "Civic", "año": 2021}
    ]
    
    # Guardar como archivo JSON
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        json.dump(vehiculos, archivo, ensure_ascii=False, indent=4)
    
    # Leer archivo JSON con pandas
    try:
        df = pd.read_json(nombre_archivo)
        print("DataFrame leído desde el archivo JSON:")
        print(df)
        print("-" * 40)
        
        # Mostrar tipos de datos
        print("Tipos de datos de cada columna:")
        print(df.dtypes)

    except ValueError as e:
        print(f"Error al leer el archivo JSON: {e}")
    except FileNotFoundError:
        print(f"Error: el archivo '{nombre_archivo}' no existe.")

# Llamar a la función
leer_json_vehiculos()
