import pandas as pd

def analizar_calificaciones():
    # Crear la Serie con índices personalizados
    calificaciones = pd.Series([85, 92, 78], 
                               index=['Matemáticas', 'Ciencias', 'Historia'])
    
    print(" Calificaciones de los estudiantes:")
    print(calificaciones)
    print("-" * 40)
    
    # Acceder a un valor específico por índice
    valor_ciencias = calificaciones['Ciencias']
    print(f" Calificación en Ciencias: {valor_ciencias}")
    print("-" * 40)
    
    # Mostrar información básica de la Serie
    print("ℹ Información de la Serie:")
    print(calificaciones.describe())  # muestra conteo, media, std, min, max
    print("-" * 40)
    
    # Calcular suma y promedio
    suma = calificaciones.sum()
    promedio = calificaciones.mean()
    print(f"🔢 Suma de calificaciones: {suma}")
    print(f"📈 Promedio de calificaciones: {promedio:.2f}")

# Llamar a la función
analizar_calificaciones()
