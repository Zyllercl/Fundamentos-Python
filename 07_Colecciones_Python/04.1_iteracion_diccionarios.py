"""
Iteración en Diccionarios
=========================

Definición:
-----------
La iteración en diccionarios permite recorrer sus elementos (pares llave-valor) de manera eficiente. Python proporciona varios métodos para facilitar esta tarea.

Métodos de Iteración:

    1. `.items()`: Este método devuelve una vista de los pares llave-valor del diccionario, permitiendo iterar sobre ambos simultáneamente.
    2. `.keys()`: Este método devuelve una vista de las llaves del diccionario, permitiendo iterar sólo sobre las llaves.
    3. `.values()`: Este método devuelve una vista de los valores del diccionario, permitiendo iterar sólo sobre los valores.
"""
# ---------------------
# Ejemplo de un diccionario
# ---------------------
persona = {
    'nombre': 'Pepe',
    'edad': 25,
    'es_mayor': True
}

print('[ITERACIÓN EN DICCIONARIOS - Método .items()]\n')
for llave, valor in persona.items():
    print(f'Llave: {llave} ;  Valor: {valor}')

print('[ITERACIÓN EN DICCIONARIOS - Método .keys()]\n')
for llave in persona.keys():
    print(f'Llave: {llave}')

print('\n[ITERACIÓN EN DICCIONARIOS - Método .values()]\n')
for values in persona.values():
    print(f'Valor: {values}')
