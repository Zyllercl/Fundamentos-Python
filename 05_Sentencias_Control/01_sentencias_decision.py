"""
Uso de sentencias de decisión en Python
=======================================
Este script muestra ejemplos de cómo utilizar las sentencias de decisión `if`, `if else` y `if elif else` en Python para controlar el flujo del programa basado en condiciones.
"""

# -----------------------------
# Ejemplos de sentencias de decisión en Python
# -----------------------------

# -----------------------------
# Ejemplo de sentencia if
# -----------------------------
print(f'[SENTENCIA IF]\n')

edad = 30

if edad >= 21:
    print(f'+ Cumples la mayoría de edad con {edad} años\n')

# ------------------------------
# Ejemplo de sentencia if else
# ------------------------------
print(f'[SENTENCIA IF ELSE]\n')

edad = 15

if edad >= 21:
    print(f'+ Cumples la mayoría de edad con {edad} años')
else:
    print(f'- Eres menor de edad, tienes {edad} años\n')

# ------------------------------
# Ejemplo de sentencia if elif else
# ------------------------------
print(f'[SENTENCIA IF ELIF ELSE]\n')

edad = 17

if edad >= 21:
    print(f'+ Cumples la mayoría de edad con {edad} años')
elif 13 <= edad < 21:
    print(f'* Eres un adolescente con {edad} años')
else:
    print(f'- Eres menor de edad, tienes {edad} años\n')