'''     DICCIONARIOS EN PYTHON    '''

print(f'-----   COLECCIONES: DICCIONARIOS   -----')
# Ejemplo de diccionarios
persona = {
    'nombre': 'Jon',
    'edad': 30,
    'es_rey': True
}

print(f'Diccionario de persona: {persona}')

# Obtener un elemento de un diccionario dependiendo de su 'llave'
print(f'\nNombre: {persona["nombre"]}')
print(f'Edad: {persona.get("edad")}')
print(f'Edad: {persona.get("es_rey")}')

# Agregar un nuevo elemento al diccionario
persona['ciudad'] = 'Winterfell'
print(f'\nAgregando un elemento al diccionario: {persona}')

# Modificar un valor del diccionario
persona['edad'] = 28
print(f'Modificar un valor de un diccionario: {persona}')

# Eliminar un elemento del diccionario
del persona['edad']
print(f'Eliminacion de un elemento del diccionario (edad): {persona}')

persona.pop('ciudad')
print(f'Diccionario persona: {persona}')

'''    Iterar los elementos de un diccionario (llave, valor)    '''

print('\n--- Método .items() ---')
# Metodo .items() permite obtener los elementos llave:valor de un diccionario
for llave, valor in persona.items():
    print(f'Llave: {llave}, Valor: {valor}')

print('\n--- Método .keys() ---')
# Metodo .keys() permite obtener sólo las llaves de un diccionario
for llave in persona.keys():
    print(f'Llave: {llave}')

print('\n--- Método .values() ---')
# Metodo .values() permite obtener sólo los valores de un diccionario
for values in persona.values():
    print(f'Valor: {values}')

