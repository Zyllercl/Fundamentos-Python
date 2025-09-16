"""
Sistema Generador de ID Único
=============================

Definición:
-----------
Generar un ID único a partir de los datos ingresados por el usuario.

Reglas para generar el ID:
1. Del valor 'nombre', usar sólo las 2 primeras letras y convertislas a mayúsculas.
2. Del valor 'apellido', usar las dos 2 primeras letras y convertirlas a mayúsculas.
3. Del valor 'año', usar los dos últimos dígitos
5. Unir los datos obtenidos en el siguiente orden:
   - Nombre (2 letras)
   - Apellido (2 letras)
   - Año (2 últimos dígitos)
   - Valor Aleatorio (4 dígitos)

Ejemplo:
-----------
    - 'nombre'          -> 'Bellamy'    -> BE
    - 'apellido'        -> 'Blake'      -> BL
    - 'año'             -> 1987         -> 87
    - 'Valor Aleatorio' -> randint()    -> 1111

    Resultado ID único: BEBL871111
"""

import random

print('-----\tGENERADOR DE ID ÚNICO\t-----\n')

# ------------------------------
# Entrada de datos
# ------------------------------
nombre = input('Ingrese su nombre: ')
apellido= input('Ingrese su apellido: ')
anho_nacimiento = input('Ingrese su fecha de nacimiento (YYYY): ')
num_aleatorio = str(random.randint(0000,9999))

# ------------------------------
# Generar partes del ID
# ------------------------------
nombre_id = nombre.strip().upper()[0:2]             # Toma los dos primeros valores, índice 0 y 1 (No considera la posición 2)
apellido_id = apellido.strip().upper()[0:2]         # Toma los dos primeros valores, índice 0 y 1 (No considera la posición 2)
anho_nacimiento_id = anho_nacimiento.strip()[2:]    # Toma los dos últimos valores, índice 2 y 3 (No considera la posición 0, 1)

# ------------------------------
# Generar ID único final
# ------------------------------
id_unico = f'{nombre_id}{apellido_id}{anho_nacimiento_id}{num_aleatorio}'

# ------------------------------
# Salida del resultado
# ------------------------------
print(f'''
    Hola {nombre},
        Tu nuevo número de idenfiticación (ID) es el siguiente:
        {id_unico}
        Felicidades!
''')