import pandas as pd

def dataframe_empleados():
    # Crear lista de diccionarios con datos de empleados
    empleados = [
        {'empleado': 'Ana', 'salario': 2500, 'departamento': 'Ventas'},
        {'empleado': 'Luis', 'salario': 3200, 'departamento': 'TI'},
        {'empleado': 'María', 'salario': 2800, 'departamento': 'Recursos Humanos'}
    ]
    
    # Convertir la lista de diccionarios a DataFrame
    df = pd.DataFrame(empleados)
    
    print("DataFrame de empleados:")
    print(df)
    print("-" * 40)
    
    # Acceder a una fila específica usando índice
    print("Fila con índice 1 (empleado 2):")
    print(df.loc[1])
    print("-" * 40)
    
    print("Varias filas (índices 0 y 2):")
    print(df.loc[[0, 2]])

# Llamar a la función
dataframe_empleados()
