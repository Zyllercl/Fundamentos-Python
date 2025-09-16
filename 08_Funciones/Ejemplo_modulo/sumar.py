"""
Uso de módulos en Python
========================
En este script se esta usando la función "sumar()" definida en el archivo ' modulo_funcion_sumar.py '
"""

from modulo_funcion_sumar import sumar

print(f'[MÓDULOS PERSONALIZADOS (SUMAR)]\n')

# -------------------------
# Llamando a la función sumar() de otro módulo
# -------------------------
resultado_funcion = sumar(5, 7)

print(f'Resultado de la función sumar: {resultado_funcion}')
