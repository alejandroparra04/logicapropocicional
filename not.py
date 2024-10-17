# Función para imprimir la tabla de verdad de la compuerta NOT
def tabla_verdad_not():
    # Imprimir encabezado de la tabla
    print("A | NOT A")
    print("--------")
    
    # Definir los valores posibles para A
    valores = [0, 1]
    
    # Iterar sobre los valores de A
    for A in valores:
        resultado = not A
        # Imprimir cada fila de la tabla
        print(f"{A} |   {int(resultado)}")

# Ejecutar la función para mostrar la tabla de verdad
tabla_verdad_not()
