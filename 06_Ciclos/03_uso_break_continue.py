"""
Uso de BREAK y CONTINUE en ciclos FOR en Python
===============================================

Definición:
-----------

Las palabras reservadas 'break' y 'continue' son utilizadas para controlar el flujo de los ciclos 'for'.

    1. break:    Permite finalizar un ciclo 'for' antes de que haya iterado sobre todos los elementos de la secuencia.
    2. continue: Permite saltarse la iteración actual y continuar con la siguiente iteración del ciclo 'for'.
"""

# ---------------------
# Ejemplo: Uso de break para salir de un ciclo for
# ---------------------
print(f'[CICLO FOR] Uso de BREAK\n')

for numero in range(1, 10):
    # Condicion: Si el numero es par, se imprime y se sale del ciclo con 'break'
    if numero % 2 == 0:
        print(numero) # Para este ejemplo, se imprimira solo el primer numero par (2) y luego se acabara el ciclo.
        break

# ---------------------
# Ejemplo: Uso de continue para saltar a la siguiente iteración en un ciclo for
# ---------------------
print(f'[CICLO FOR] Uso de CONTINUE\n')

for numero in range(1, 10):
    # Condición: Si el numero es impar, se salta a la siguiente iteración con 'continue', es decir, no se ejecuta el print(numero) cuando el número es impar.
    if numero % 2 == 1:
        continue
    
    # Si el número es par, se imprime
    print(numero)