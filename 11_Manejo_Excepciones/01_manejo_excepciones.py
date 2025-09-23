"""
Manejo de Excepciones en Python
===============================
Este script muestra cómo manejar excepciones comunes en Python utilizando bloques try-except.
"""

from excepcion_personalizada import NumerosIgualesError

# --------------------------
# Ejemplo: Manejo de Excepciones
# --------------------------
print(f'[EJEMPLO] Manejo de Excepciones\n')

# Variables Globales
resultado = None

try:
    # Variables Locales
    a = int(input("Ingrese un número (a): ")) 
    b = int(input("Ingrese un número (b): "))  # Puede ser cualquier valor

    # Validación personalizada (a == b)
    if a == b:
        # raise -> Permite lanzar una excepcion ya definida y excepciones personalizada
        raise NumerosIgualesError("¡Los números no pueden ser iguales!")

    resultado = a / b  # Esto puede generar ZeroDivisionError, TypeError u otro error
except ZeroDivisionError as e:
    print(f"[ERROR] {e} , {type(e)}")
except TypeError as e:
    print(f"[ERROR] {e} , {type(e)}")
except Exception as e:
    print(f"[ERROR] Ocurrió una excepción inesperada: {e} , {type(e)}")
else:
    print("\n[ELSE] La operación se realizó correctamente, no se produjeron errores.")
finally:
    print("\n[FINALLY] Fin del bloque try-except, se ejecuta siempre.")

print(f"\n[RESULTADO] {resultado}")
print(f'Continuando con el programa...')