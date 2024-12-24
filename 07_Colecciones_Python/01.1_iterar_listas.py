'''     ITERAR LISTAS EN PYTHON    '''

print(f'-----   COLECCIONES: ITERAR LISTAS   -----')
# Ejemplo 1: Iterar listas
nombres = ['Jon', 'Arya', 'Sansa']
i = 0

for nombre in nombres:
    print(f'Posicion [{i}]: {nombre}')
    i += 1

print()

# Ejemplo 2: Iterar listas
lista_mixta = [100, False, 'Varys']
i = 0

for lista in lista_mixta:
    print(f'Posicion [{i}]: {lista}')
    i += 1
