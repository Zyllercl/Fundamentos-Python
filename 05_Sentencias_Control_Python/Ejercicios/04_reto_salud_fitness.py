"""
RETO: Aplicación de Salud y Fitness
===================================

Definición:
-----------

Crear una aplicación que solicite lo siguiente:

    1. Nombre de usuario
    2. Pasos caminados en el día

Además, se deberá definir las siguientes constantes:
    - META_PASOS_DIARIO = 10000
    - CALORIAS_POR_PASO = 0.04  # Valor aproximado en kilocalorias

Para calcular las calorías quemadas se debe ocupar la siguiente fórmula:
    - calorias_quemadas = pasos_diarios * CALORIAS_POR_PASO

Y se verifica si se cumplió la meta de pasos diarios con la siguiente fórmula:
    - meta_alcanzada = pasos_diarios >= META_PASOS_DIARIO

*Aplicar operador ternario para determinar si se alcanzó la meta de pasos diarios.*
"""

print(f'[APLICACIÓN FITNESS]\n')

# -----------------------------
# Definición de constantes
# -----------------------------
META_PASOS_DIARIO = 10000
CALORIAS_POR_PASO = 0.04

# -----------------------------
# Solicitar datos al usuario
# -----------------------------
nombre_usuario = input('Ingrese su nombre: ')
pasos_diarios = int(input('Cuantos pasos has caminado hoy?: '))

# -----------------------------
# Cálculos de calorías quemadas y meta alcanzada
# -----------------------------
calorias_quemadas = pasos_diarios * CALORIAS_POR_PASO
meta_alcanzada = pasos_diarios >= META_PASOS_DIARIO
meta_alcanzada = "Si" if meta_alcanzada else "No"

print(f'''\nINFORMACIÓN FITNESS\n
Usuario: {nombre_usuario}
N° Pasos: {pasos_diarios}
Calorias quemadas: {calorias_quemadas} Kcal
Pasos diarios alcanzados: {meta_alcanzada}
Meta de pasos diario: {META_PASOS_DIARIO}\n
''')
