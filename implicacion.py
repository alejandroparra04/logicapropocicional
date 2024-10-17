def tabla_verdad_implicacion():
    print("A | B | A → B")
    print("-------------")
    for A in [0, 1]:
        for B in [0, 1]:
            resultado = not A or B
            print(f"{A} | {B} |   {int(resultado)}")

tabla_verdad_implicacion()