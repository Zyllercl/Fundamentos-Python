"""
Uso de función RANGE en Python - Números
========================================

Definición:
-----------

La función 'range' es una función incorporada que genera una secuencia de números. Se utiliza comunmente para iterar sobre ciclos de tipo 'for'.

Sintaxis:
---------

    range(inicio, fin, incremento)
        Donde:
            - inicio:       Valor inicial (opcional, por defecto es 0)
            - fin:          Valor final (sin incluirlo)
            - incremento:   Diferencia entre cada número (opcional, por defecto es 1)
"""

print(f'[FUNCION RANGE - NUMEROS]\n')

# ---------------------
# Ejemplo: Usa range para imprimir del 0 al 4
# ---------------------
print('[+] Secuencia del 0 al 4:')

# ----------------------
# inicio = 0 (opcional)
# fin = 5 - 1 = 4
# incremento = 1 (opcional)
# ---------------------
for i in range(5):
    print(i, end=' ')

# ---------------------
# Ejemplo: Usa range para imprimir del 1 al 10
# ---------------------
print('\n[+] Secuencia del 1 al 10:')

# ----------------------
# incremento = 1 (default)
# ----------------------
for i in range(1, 10 + 1):
    print(i, end=' ')

# ---------------------
# Ejemplo: Usa range para imprimir del 0 al 9 con incremento de 2
# ---------------------
print('\n[+] Secuencia del 0 al 9 con incremento 2:')
# ----------------------
# inico = 0
# fin = 10
# incremento = 2
# ----------------------
for i in range(0, 10, 2):
    print(i, end=' ')

print()  # Salto de línea final