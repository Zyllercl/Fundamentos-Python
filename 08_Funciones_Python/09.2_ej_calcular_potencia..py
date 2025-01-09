'''
    CALCULAR LA POTENCIA DE UN NUMERO

    Def:
        - Crear una función recursiva para que calcule la potencia de un npumero utilizando la siguiente formul:

            Formula: a² = a * a^(b - 1)

            Donde "a" es la base y "b" es la potencia, es decir, se debe multiplicar "a" por si mismo "b" veces.

        Ej:
            2³ = 2 * 2 * 2 = 8
'''

print(f'-----   CALCULAR LA POTENCIA DE UN NUMERO  -----\n')

def potencia(base, exponente):
    # Caso base
    if exponente == 0:
        return 1
    else:
        # Caso recursivo
        return base * potencia(base, exponente -1)

print(f'Potencia de 2 elevado a 3 es: {potencia(2, 3)}')
print(f'Potencia de 5 elevado a 0 es: {potencia(5, 0)}')