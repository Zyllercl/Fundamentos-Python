from excepciones_personalizadas import NumerosIdenticos

# [ERROR] ZeroDivisionError: division by zero
""" division_cero = 10/0 
print(division_cero)  """

# Variables Globales
resultado = None

# Manejo de Excepciones
try:
    # Variables dentro del Try (no son accesibles fuera del Try)
    a = int(input('Ingresa el primer numero: '))
    b = int(input('Ingresa el segundo numero: '))
    
    if a == b:
        # raise -> Permite lanzar o arrojar una excepcion (Especificas o Personalizadas)
        raise NumerosIdenticos('[ERROR] Numeros Identicos')
    
    resultado = a / b
    
except ZeroDivisionError as e:
    print(f'[ZeroDivisionError] Ocurrio un error -> {e} , {type(e)}')
# Excepciones Especificas
except TypeError as e:
    print(f'[TypeError] Ocurrio un error -> {e} , {type(e)}')
except ValueError as e:
    print(f'[ValueError] Ocurrio un error -> {e} , {type(e)}')
# Excepcion Generica (debe ir al final de las excepciones hijas)
except Exception as e:
    print(f'[Exception] Ocurrio un error -> {e} , {type(e)}')
# Se va a ejecutar si no se a lanzado ninguna excepcion
else:
    print('No se arrojo ninguna exepcion')
# Siempre se va a ejecutar independientemente si se lanza una excepcion o no
finally:
    print('Finalizacion del programa')

print(f'Resultado: {resultado}') # La variable 'resultado' mantiene su valor inicial
print('Continuacion..')