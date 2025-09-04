"""
Ejemplo: Función que Retorna Varios Valores
==================================

Definición:
-----------

- En Python una función puede devolver más de un valor al mismo tiempo.

- Los valores que se devuelven empaquetados en una tupla, la cual puede luego ser desempaquetada en variables individuales.

- Este tipo de funciones resulta útil cuando una función necesita entregar varios resultados relacionados.
"""

print(f'[EJEMPLO] Función que Retorna Varios Valores\n')

# ---------------------------
# Definicion de la función
# ---------------------------
def persona_mayusculas(nombre, apellido, edad):
    print(f'Esta función retornará varios valores (tupla)\n')

    return nombre.upper(), apellido.upper(), edad
# ---------------------------
# Desempaquetamiento (Unpacking)
# ---------------------------
nombre, apellido, edad = persona_mayusculas('sansa', 'stark', 28)

print(f'Resultado: \nNombre = {nombre} \nApellido = {apellido} \nEdad = {edad}')