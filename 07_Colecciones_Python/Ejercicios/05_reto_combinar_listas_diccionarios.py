"""
RETO: Combinación de listas y diccionarios
==========================================

Definición:
-----------

Crear un programa en donde se almacenen de una lista, diferentes diccionarios en su interior.
"""

print(f'[RETO] Combinación de listas y diccionarios')

# -------------------
# Creación de la lista con diccionarios en su interior
# -------------------
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

# -------------------
# Acceder a un diccionario desde una lista (Ej: primera posición)
# -------------------
print(f'''\nInformación diccionario dentro de una lista
    Nombre: {personas[0].get('nombre')}
    Apellido: {personas[0].get('apellido')}
    Edad: {personas[0].get('edad')}
''')

# -------------------
# Recorrer elementos de la lista
# -------------------
print(f'Recorriendo la lista de diccionarios: \n')

for contador, persona in enumerate(personas):
    # -------------------
    # Método enumerate: Permite enumerar los registros iterados con un contador automático. Se usa comunmente en tuplas, listas, diccionarios, cadenas, etc.
    # -------------------
    print(f'{contador} - {persona}')
    print(f'Detalle: {persona.get("nombre")} {persona.get("apellido")}\n')