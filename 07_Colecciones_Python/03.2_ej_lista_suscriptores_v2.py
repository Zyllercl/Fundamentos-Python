'''
    LISTA DE SUSCRIPTORES V2

    Def: 
        - Crea un programa para administrar una lista de suscriptores utilizando un email. Imaginemos que un usuario se suscribe al boletín informativo del díario utilizando su correo electronico. Además, hay que asegurarse de que no existan suscriptores duplicados y se debe considerar poder agregar y eliminar suscriptores.
'''

print(f'-----   SUSCRIPCION BOLETIN INFORMATIVO   -----')
# Variables
suscriptores = set()
num_suscriptores = int(input('Ingresa el número de suscriptores iniciales: '))

for _ in range(num_suscriptores):
    suscriptores.add(input('Suscriptores iniciales (email): '))

print(f'\nLista de suscriptores inicial: {suscriptores}')

# Verificar si un nuevo suscriptor se encuentra en la lista
nuevo_suscriptor = input('Ingresar nuevo suscriptor (email): ')

if nuevo_suscriptor in suscriptores:
    print(f'\nEl nuevo suscriptor ya se encuentra en la lista: {nuevo_suscriptor}')
else:
    suscriptores.add(nuevo_suscriptor)
    print(f'\nEl nuevo suscriptor se a agregado a la lista: {nuevo_suscriptor}')

print(f'\nLista de suscriptores: {suscriptores}')

# Eliminar un suscriptor existente
eliminar_suscriptor = input('Eliminar suscriptor (email): ')
suscriptores.remove(eliminar_suscriptor)

print(f'\nEl suscriptor {eliminar_suscriptor} ha sido eliminado de la lista!')
print(f'\nLista de suscriptores: {suscriptores}')

# Verificamos la cantidad total de suscriptores
print(f'\nCantidad total suscriptores: {len(suscriptores)}')

# Mostrar lista suscriptores
print(f'\n--- Lista de Suscriptores ---')
i = 1

for suscriptor in suscriptores:
    print(f'Suscriptor {i}: {suscriptor}')
    i += 1