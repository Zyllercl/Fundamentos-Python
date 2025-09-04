"""
Ejemplo: Calcular la Potencia de un número
==========================================

Definición:

Crear una función recursiva que permita calcular la potencia de un número utilizando la siguiente formula:

    [FORMULA]
    
    a² = a * a^(b - 1)

    Donde:
        a : Base
        b : Potencia

    Ejemplo:
        2³ = 2 * 2 * 2 = 8
"""

print(f'[EJEMPLO] Calcular la Potencia de un número\n')

# -----------------------
# Definición Función Recursiva
# -----------------------
def potencia(base, exponente):
    # Excepciones: Si el exponente es 0, el valor es 1.
    if exponente == 0:
        return 1
    else:
        # Aplicando Recursividad
        return base * potencia(base, exponente -1)

print(f'Potencia de 2 elevado a 3 es: {potencia(2, 3)}\n')
print(f'Potencia de 5 elevado a 0 es: {potencia(5, 0)}')