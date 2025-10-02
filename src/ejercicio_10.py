import requests
import pandas as pd

def dataframe_desde_api():
    url = "https://playground.mockoon.com/users"
    
    try:
        # Hacer la petición GET
        response = requests.get(url, timeout=10)
        
        # Verificar que la respuesta fue exitosa
        if response.status_code == 200:
            # Convertir JSON a DataFrame
            df = pd.DataFrame(response.json())
            
            print("Primeras 5 filas del DataFrame:")
            print(df.head())
            print("-" * 40)
            
            # Mostrar información básica del DataFrame
            print("Información del DataFrame:")
            print(df.info())
        else:
            print(f"Error: la petición falló con código {response.status_code}")
    
    except requests.exceptions.RequestException as e:
        print(f"Error de conexión: {e}")

# Llamar a la función
dataframe_desde_api()
