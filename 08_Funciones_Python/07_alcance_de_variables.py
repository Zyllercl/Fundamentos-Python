'''
    ALCANCE DE VARIABLES 

    Def:
        - Las variables pueden tener un alcance global o local dependiendo de dónde y cúando se declaren:
        
            1. Variables Globales:  Son aquellas que están disponibles a lo largo de todo el programa.

            2. Variables Locales:   Son aquellas que están disponibles dentro del bloque de código o función donde fueron declaradas.
'''

print(f'-----   ALCANCE DE VARIABLES   -----')

# Variables Globales
contador_global = 0

def incrementar_contador():
    # Variables Locales
    contador_local = 0
    # Uso variable global
    global contador_global
    # Incremento de Variable Global
    contador_global += 1
    # Incremento de Variable Local
    contador_local += 1

    # Imprimiendo ambos contadores
    print(f'Contador Local: {contador_local}')
    print(f'Contador Global: {contador_global}')

# Llamada a la funcion varias veces
incrementar_contador() # Cabe destacar que la variable local se reiniciará cada vez que se llama a la función.
incrementar_contador()
incrementar_contador()
incrementar_contador()

# Sólo se puede imprimir la Variable Global, ya que la variable Local sólo se puede ocupar dentro de la función.
print(f'Variable_global: {contador_global}')