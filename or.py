# Función para imprimir la tabla de verdad de la compuerta OR
def tabla_verdad_or():
    # Imprimir encabezado de la tabla
    print("A | B | A OR B")
    print("-------------")
    
    # Definir los valores posibles para A y B
    valores = [0, 1]
    
    # Iterar sobre cada combinación de valores
    for A in valores:
        for B in valores:
            resultado = A or B
            # Imprimir cada fila de la tabla
            print(f"{A} | {B} |   {resultado}")

# Ejecutar la función para mostrar la tabla de verdad
tabla_verdad_or()
