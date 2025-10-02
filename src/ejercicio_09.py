import numpy as np
import pandas as pd

def dataframe_desde_numpy():
    # Crear un array NumPy 2D con datos de ventas trimestrales
    array_numpy = np.array([
        [1500, 2000, 2500],
        [1800, 2200, 2600],
        [1700, 2100, 2400]
    ])
    
    # Crear el DataFrame con nombres de columnas
    df = pd.DataFrame(array_numpy, columns=['Q1', 'Q2', 'Q3'])
    
    print("DataFrame de ventas trimestrales:")
    print(df)
    print("-" * 40)
    
    # Verificar tipos de datos
    print("Tipos de datos en el DataFrame:")
    print(df.dtypes)

# Llamar a la función
dataframe_desde_numpy()
