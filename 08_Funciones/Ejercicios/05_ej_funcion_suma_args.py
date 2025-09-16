"""
Ejemplo: Funcion que Suma con Argumentos Variables (*args)
==========================================================

Definición:
-----------

Crear una función para que acepte Argumentos Variables, posterior realizar la suma de los valores ingresados.
"""

print(f'[EJEMPLO] Suma con Argumentos Variables\n')

# ---------------------
# Declaración función con *args
# ---------------------
def sumar_args_variables(*args):
    # Variable Local
    total = 0

    for numero in args:
        # print(f'Numero Actual: {numero}')
        total += numero
        # print(f'Valor Total Temporal: {total}\n')
    
    return total

# ---------------------
# Llamando a la función
# ---------------------
resultado = sumar_args_variables(1, 2, 3, 4, 5)

print(f'Resultado Final: {resultado}')