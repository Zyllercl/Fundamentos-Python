'''
    COMBINACION DE LISTAS Y DICCIONARIOS

    Def:
        - Crear un rograma en donde se almacenen de una lista, diferentes diccionarios en su interior.
'''

print(f'-----   COMBINACION DE LISTAS Y DICCIONARIOS   -----')
# Variables
personas = [
    {
        'nombre': 'Homero',
        'apellido': 'Simpson',
        'edad': 52
    },
    {
        'nombre': 'Marge',
        'apellido': 'Simpson',
        'edad': 50
    }
]

# Acceder a un diccionario desde una lista
print(f'''\nInformación diccionario dentro de una lista
    Nombre: {personas[0].get('nombre')}
    Apellido: {personas[0].get('apellido')}
    Edad: {personas[0].get('edad')}
''')

# Recorrer elementos de la lista
for contador, persona in enumerate(personas):
    # Metodo enumerate -> Permite enumerar los registros iterados con un contador automático. Se usa comunmente en tuplas, listas, diccionarios, cadenas, etc.
    print(f'{contador} - {persona}')
    print(f'Detalle: {persona.get("nombre")} {persona.get("apellido")}')