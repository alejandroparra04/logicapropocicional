def tabla_verdad_bicondicional():
    print("A | B | A ↔ B")
    print("-------------")
    for A in [0, 1]:
        for B in [0, 1]:
            resultado = A == B
            print(f"{A} | {B} |   {int(resultado)}")

tabla_verdad_bicondicional()
