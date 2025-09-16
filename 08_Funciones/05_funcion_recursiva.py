"""
Funciones Recursivas en Python
==============================
Este script muestra un ejemplo de como funciona la función recurvisa.
"""

print(f'[FUNCIÓN RECURVISA]\n')

# ------------------------
# Declaración Función Recursiva
# ------------------------
def funcion_recursiva(numero):
    # Caso Base
    if numero == 1:
        print(numero, end= ' ') # Termina el ciclo hasta llegar a 1
    else:
        print(numero) # Orden DESC
        # Llamada a si misma
        funcion_recursiva(numero - 1)
        
# ------------------------
# Llamada a funcion recursiva
# ------------------------
funcion_recursiva(5)
print() # Salto de línea al final

    


