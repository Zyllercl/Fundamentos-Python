"""
RETO: Agenda de contactos
=========================

Definición:
-----------

Crea una agenda de contactos utiizando un diccionario con la siguiente estructura:

    agenda {
        nombre {
            telefono
            correo
            direccion
        }
    }
"""

print(f'[RETO] Agenda de contactos\n')

# -------------------
# Creación del diccionario
# -------------------
agenda = {
    'Homero': {
        'telefono': '11223344',
        'direccion': 'Bar Moe',
        'correo': 'homero@simpson.com'
    },
    'Marge': {
        'telefono': '55667788',
        'direccion': 'Avenida Siempreviva',
        'correo': 'marge@simpson.com'
    },
    'Bart': {
        'telefono': '12345678',
        'direccion': 'Escuela Springfield',
        'correo': 'bart@simpson.com'
    },
}

print(f'Agenda: \n{agenda}')

# -------------------
# Acceder a la información de un contacto específico
# -------------------
print(f'''\nInformación del contacto Homero:
    Dirección: {agenda["Homero"]['direccion']}
    Correo: {agenda.get('Homero').get('correo')}
    Telefono: {agenda.get('Homero').get('telefono')}
''')

# -------------------
# Agregar un nuevo contacto al diccionario
# -------------------
agenda['Lisa'] = {
    'telefono': '77889900',
    'direccion': 'Avenida Siempreviva',
    'correo': 'lisa@simpson.com'
}

print(f'Agregando nuevo contacto (Lisa): \n{agenda}')

# -------------------
# Eliminar un registro existente
# -------------------
agenda.pop('Marge') # Forma 1

# del agenda['Marge'] # Forma 2

print(f'\nEliminando un contacto (Marge): \n{agenda}')

# -------------------
# Mostrar los contactos de la agenda
# -------------------
for nombre, detalle in agenda.items():
    print(f'''\nDetalle del contacto {nombre}:
        Telefóno: {detalle.get('telefono')}.
        Dirección: {detalle.get('direccion')}.
        Correo: {detalle.get('correo')}.
''')