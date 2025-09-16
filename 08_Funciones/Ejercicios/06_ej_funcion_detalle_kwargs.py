"""
Ejemplo: Detalle de Personas con Argumnetos Variables (**kwargs)
================================================================

Definición:
-----------

Crear una función que acepte Argumentos Variables (**kwargs) en forma de ` llave : valor ` (Diccionario).
"""

print(f'[EJEMPLO] Detalle de Personas con Argumentos Variables')

# ---------------------
# Declaración función con **kargs
# ---------------------
def detalle_persona(**kwargs):
    print()
    for llave, valor in kwargs.items():
        print(f'{llave} : {valor}')

# ---------------------
# Llamada a la función
# ---------------------
detalle_persona(nombre = 'Octavia', apellido = 'Blake', edad = 29)
detalle_persona(nombre = 'Bellamy', apellido = 'Blake', edad = 32)
