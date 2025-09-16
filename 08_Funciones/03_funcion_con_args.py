"""
Función con argumentos variables (*args)
========================================

Definición:
-----------
Argumentos Posicionales Variables ( *args ): Permite pasar múltiples argumentos posicionales a una función, esstos se reciben como una Tupla '()' dentro de una función.
"""

print(f'[FUNCION CON *ARGS]')

# ---------------------
# Definición de una función
# --------------------- 
def superheroe_superpoderes(superheroe, nombre, *args):
    # El parametro *args se tomará como los 'superpoderes', es decir, que puede tener 1 o más en forma de tupla.
    print(f'\nSuperheroe: {superheroe} - {nombre} - {args}')

    # Iterar la tupla de *args (Superpoderes)
    for superpoder in args:
        print(f'\tSuperpoder: {superpoder}')

# ---------------------
# Llamando a la funcion
# Sintaxis: superheroe_superpoderes( 'SUPERHEROE', 'NOMBRE_SUPERHEROE', 'args1', 'args2', 'args3'... )
# ---------------------
superheroe_superpoderes('Spiderman', 'Peter Parker', 'Telaraña', 'Instinto Arácnido')

superheroe_superpoderes('Iron Man', 'Tony Stark', 'Armadura', 'Millonario', 'Volar')

# ---------------------
# Llamada a la función sin entregar argumentos variables *args
# ---------------------
superheroe_superpoderes('Guardianes de la Galaxia', 'Groot')