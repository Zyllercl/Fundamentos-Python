"""
RETO: Casa Embrujada
====================

Definición:
-----------

Crear un programa que determine si un usuario puede ingresar a una casa embrujada en Fantasilandia. Para ello, se deben cumplir las siguientes condiciones:

    1. El usuario debe tener más de 10 años.
    2. El usuario no debe tener miedo a la oscuridad.

Si se cumplen ambas condiciones, el usuario puede ingresar; de lo contrario, no puede ingresar.
"""

print(f'[CASA EMBRUJADA] - Fantasilandia\n')

# -----------------------------
# Solicitar datos al usuario
# -----------------------------
edad = int(input('Ingrese su edad: '))
fobia_oscuridad = input('Le tienes miedo a la oscuridad? (Si/No): ')

# -----------------------------
# Tratamiento de la variable fobia_oscuridad
# -----------------------------
fobia_oscuridad = (fobia_oscuridad.strip().lower() == 'si')

# -----------------------------
# Validar condiciones para ingresar a la Casa Embrujada
# -----------------------------
if not fobia_oscuridad and edad >= 10:
    print('El usuario puede ingresar a la Casa Embrujada')
else:
    print('El usuario NO puede ingresar a la Casa Embrujada...')
