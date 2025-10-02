import pandas as pd

def analizar_ventas():
    # Crear la Serie de ventas diarias
    ventas = pd.Series([150, 200, 180, 220, 175, 190, 165], 
                       index=["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"])
    
    print(" Ventas diarias (Serie):")
    print(ventas)
    print("-" * 40)
    
    # Acceder al valor del índice 3
    valor_indice_3 = ventas[3]
    print(f" Valor en el índice 3 (Jue): {valor_indice_3}")
    print("-" * 40)
    
    # Calcular el promedio de ventas
    promedio = ventas.mean()
    print(f" Promedio de ventas: {promedio:.2f}")
    print("-" * 40)
    
    # Ordenar la Serie por valores
    ordenadas = ventas.sort_values()
    print(" Ventas ordenadas de menor a mayor:")
    print(ordenadas)


# Llamar a la función
analizar_ventas()
