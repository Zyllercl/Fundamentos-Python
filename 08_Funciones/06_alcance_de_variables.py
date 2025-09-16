"""
Uso del Alcance de Variables
============================
En este script se realiza un ejemplo del alcance de las variables, existen dos tipos:

    1. Variables Globales: Son aquellas que están disponibles a lo largo de todo el programa.
    2. Variables Locales:  Son aquellas que están disponibles dentro del bloque de código o función donde fueron declaradas.
"""

print(f'[ALCANCE DE VARIABLES GLOBALES Y VARIABLES LOCALES]\n')

# ----------------------
# Variables Globales
# ----------------------
contador_global = 0

# ----------------------
# Creacicón de la función
# ----------------------
def incrementar_contador():
    # ----------------------
    # Variables Locales
    # ----------------------
    contador_local = 0

    # Uso variable global
    global contador_global
    
    # Incremento de Variable Global
    contador_global += 1
    # Incremento de Variable Local
    contador_local += 1

    # Imprimiendo ambos contadores
    print(f'Contador Local: {contador_local}')
    print(f'Contador Global: {contador_global}\n')

# ----------------------
# Llamada a la funcion varias veces
# ----------------------
incrementar_contador() # Cabe destacar que la variable local se reiniciará cada vez que se llama a la función.
incrementar_contador()
incrementar_contador()
incrementar_contador()

# ----------------------
# Mostrar el valor de la Variable Global
# ----------------------
print(f'Variable Gobal: {contador_global}')

# ----------------------
# Mostrar el valor de la Variable Local
# ----------------------
# print(f'variable Local: {contador_local}')    [ERROR] Ya que la variable se encuentra dentro de la función.