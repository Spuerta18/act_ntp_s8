import pandas as pd

def dataframe_libros():
    # Crear lista de listas con datos de libros
    datos = [
        ['Cien años de soledad', 'Gabriel García Márquez', 1967],
        ['Don Quijote de la Mancha', 'Miguel de Cervantes', 1605],
        ['La ciudad y los perros', 'Mario Vargas Llosa', 1963]
    ]
    
    # Definir nombres de las columnas
    nombres_columnas = ['Titulo', 'Autor', 'Año']
    
    # Crear el DataFrame
    df = pd.DataFrame(datos, columns=nombres_columnas)
    
    print("DataFrame de libros:")
    print(df)
    print("-" * 40)
    
    # Mostrar dimensiones del DataFrame
    print("Dimensiones del DataFrame (filas, columnas):")
    print(df.shape)

# Llamar a la función
dataframe_libros()
