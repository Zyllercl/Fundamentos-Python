"""
Función con argumentos variables (**kwargs)
========================================

Definición:
-----------
Argumentos con 'Palabra Clave' ( **kwargs ): Recibe los argumentos en forma de Diccionario (llave:valor). 
"""

print(f'[FUNCION CON **KWARGS]\n')


# ---------------------
# Definición de una función
# --------------------- 
def superheroe_superpoderes(nombre, *args, **kwargs):
    print(f'Superheroe: {nombre} - {args} - Más info: {kwargs}\n')

# --------------------- 
# Llamada a la función
# --------------------- 
superheroe_superpoderes('Spiderman', 'Instinto Aracnido', edad = 27, empresa = 'Marvel')
superheroe_superpoderes('Iron Man', 'Armadura', 'Volar', edad = 38)