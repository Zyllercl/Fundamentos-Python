"""
Sistema de prestamos
========================

Definición:
-----------

Una biblioteca ofrece préstamos de libros a usuarios que cumplan con al menos una de las siguientes condiciones:
1. El usuario tiene credencial de estudiante.
2. El usuario vive a no más de 3Km a la redonda de la biblioteca

Si cumple con cuaquiera de estas condiciones, se le puede prestar el libro.
"""

# ---------------------------
# Ejemplo de uso del operador OR
# ---------------------------
print(f'[SISTEMA DE PRESTAMOS]\n')

# ---------------------------
# Entrada de datos
# ---------------------------
DISTANCIA_REDONDA = 3
es_estudiante = input('Tienes credencial estudiantil? (Si/No): ')
distancia = int(input('A cuantos Km vives de la biblioteca?: '))

resultado = (distancia <= DISTANCIA_REDONDA) or (es_estudiante.strip().lower() == 'si')

print(f'¿Puedo tomar prestado un libro?: {resultado}')