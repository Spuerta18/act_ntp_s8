import pandas as pd

def crear_dataframe():
    # Crear diccionario con productos
    datos = {
        'Producto': ['Laptop', 'Smartphone', 'Tablet'],
        'Precio': [3500, 1200, 800],
        'Categoria': ['Electrónica', 'Electrónica', 'Electrónica']
    }
    
    # Convertir a DataFrame
    df = pd.DataFrame(datos)
    
    print("DataFrame de productos:")
    print(df)
    print("-" * 40)
    
    # Acceder a la columna 'Precio'
    print("Columna de precios:")
    print(df['Precio'])
    print("-" * 40)
    
    # Información básica del DataFrame
    print("Información del DataFrame:")
    print(df.info())

# Llamar a la función
crear_dataframe()
