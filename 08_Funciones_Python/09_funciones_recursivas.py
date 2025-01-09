'''
    FUNCIONES RECURSIVAS 

    Def:
        - Los funciones recursivas deben cumplir las siguientes reglas:

            1.- Una función que se llama a si misma
            2.- Debe avanzar hacia el caso base, de lo contrario se cae en ciclos infinitos. Con cada llamada recursiva nos acercamos al caso base

                Sintaxis función recursiva

                    mi_funcion(n):
                        if n == 1:
                            regresa n
                        else:
                            mi_funcion(n-1)

'''

print(f'-----   FUNCIONES RECURSIVAS   -----')

# Funcion Recursiva

def funcion_recursiva(numero):
    # Caso Base
    if numero == 1:
        print(numero, end= ' ') # Termina el ciclo hasta llegar a 1
    else:
        # Caso recursivo
        print(numero, end= ' ') # Orden DESC
        funcion_recursiva(numero - 1)
        

# Llamada a funcion recursiva
funcion_recursiva(5)
print()

    


