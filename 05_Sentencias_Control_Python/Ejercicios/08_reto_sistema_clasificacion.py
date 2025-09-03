"""
RETO: Sistema de Clasificación
==============================

Definición:
-----------

Crear un programa para convertir una calificación numérica entre (1.0 y 7.0) a una letra. Considerar las siguientes condiciones:

    1. Si la nota es igual a 1.0 y menor o igual a 3.9             -> Letra F
    2. Si la nota es mayor o igual a 4.0 y menor o igual que 4.9   -> Letra D
    3. Si la nota es mayor o igual a 5.0 y menor o igual a 5.9     -> Letra C
    4. Si la nota es mayor o igual a 6.0 y menor o igual a 6.5     -> Letra A
    5. Si la nota es mayor a 6.5 y menor o igual a 7.0             -> Letra A+
"""

print(f'[SISTEMA DE CLASIFICACIÓN]\n')

# -----------------------------
# Solicitar nota al usuario
# -----------------------------
nota = float(input('Ingrese su nota entre 1.0 y 7.0: '))
letra = None

# -----------------------------
# Validar la nota y asignar la letra correspondiente
# -----------------------------
if nota == 1.0 or nota <= 3.9:
    letra = 'F'
elif 4.0 <= nota <= 4.9:
    letra = 'D'
elif 5.0 <= nota <= 5.9:
    letra = 'C'
elif 6.0 <= nota <= 6.5:
    letra = 'A'
elif 6.5 < nota <=  7.0:
    letra = 'A+'
else:
    print(f'La nota {nota} no es valida...')

print(f'''\n
La nota {nota:.2f} corresponde a una: {letra}
''')