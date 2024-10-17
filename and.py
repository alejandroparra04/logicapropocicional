# Función para imprimir la tabla de verdad de la compuerta AND
def tabla_verdad_and():
    print("A | B | A AND B")
    print("--------------")
    # Posibles valores de entrada (A, B)
    for A in [0, 1]:
        for B in [0, 1]:
            resultado = A and B
            print(f"{A} | {B} |   {resultado}")

# Llamar a la función para imprimir la tabla de verdad
tabla_verdad_and()
