'''
    AGENDA DE CONTACTOS

    Def: 
        - Crea una agenda de contactos utiizando un diccionario con la siguiente estructura:

            agenda {
                nombre {
                    telefono
                    correo
                    direccion
                }
            }
'''

print(f'-----   AGENDA DE CONTACTOS   -----')
# Variables
agenda = {
    'Homero': {
        'telefono': '3344556666',
        'direccion': 'Bar Moe',
        'correo': 'homero@simpson.com'
    },
    'Marge': {
        'telefono': '1122334455',
        'direccion': 'Avenida Siempreviva',
        'correo': 'marge@simpson.com'
    },
    'Bart': {
        'telefono': '777888999',
        'direccion': 'Escuela Springfield',
        'correo': 'bart@simpson.com'
    },
}

print(f'{agenda}')

# Acceder a la información de un contacto específico
print(f'''\nInformacion del contacto Homero:
    Dirección: {agenda["Homero"]['direccion']}
    Correo: {agenda.get('Homero').get('correo')}
    Telefono: {agenda.get('Homero').get('telefono')}
''')

# Agregar un nuevo contacto al diccionario
agenda['Lisa'] = {
    'telefono': '77889900',
    'direccion': 'Avenida Siempreviva',
    'correo': 'lisa@simpson.com'
}

print(f'Agregando nuevo contacto (Lisa): {agenda}')

# Eliminar un registro existente
# agenda.pop('Marge')
del agenda['Marge']

print(f'\nEliminando un contacto (Marge): {agenda}')

# Mostrar los contactos de la agenda
for nombre, detalle in agenda.items():
    print(f'''
        Telefóno: {detalle.get('telefono')}.
        Dirección: {detalle.get('direccion')}.
        Correo: {detalle.get('correo')}.
''')