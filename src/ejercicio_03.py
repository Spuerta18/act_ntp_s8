import pandas as pd

def operaciones_series():
    # Crear las Series de precios y descuentos
    precios = pd.Series([100, 150, 200], index=['Producto A', 'Producto B', 'Producto C'])
    descuentos = pd.Series([10, 20, 15], index=['Producto A', 'Producto B', 'Producto C'])
    
    print(" Precios originales:")
    print(precios)
    print("-" * 40)
    
    print(" Descuentos:")
    print(descuentos)
    print("-" * 40)
    
    # Resta entre precios y descuentos
    precios_finales = precios - descuentos
    print(" Precios después de aplicar descuentos (elemento por elemento):")
    print(precios_finales)
    print("-" * 40)
    
    # Multiplicar precios por un escalar (ejemplo: aplicar IVA del 16%)
    precios_con_iva = precios * 1.16
    print(" Precios con IVA (16%):")
    print(precios_con_iva)
    print("-" * 40)
    
    # Mostrar ejemplo de operación elemento por elemento
    print("🔎 Demostración de operación elemento por elemento (Precio - Descuento):")
    for producto in precios.index:
        print(f"{producto}: {precios[producto]} - {descuentos[producto]} = {precios_finales[producto]}")

# Llamar a la función
operaciones_series()
