"""
Uso de Entrada de Datos en Python
=================================
Este script muestra cómo recibir diferentes tipos de datos desde la consola en Python.
"""


# -------------------------------------
# Entrada de Datos desde la Consola
# -------------------------------------

# Entrada de dato String
nombre_usuario = input('Ingresa nombre de usuario: ')

# Entrada de dato Númerico
edad_usuario = int(input('Ingresa tu edad: '))

# Entrada de dato Flotante
sueldo_usuario = float(input('Ingresa tu sueldo: '))

# Entrada de dato Booleano
es_trabajador = input('¿Cargo de Jefe (Si/No)?: ')
# Conversión de String a Booleano
es_trabajador = es_trabajador.strip().lower() == 'si'

# -------------------------------------
# Mostrar los datos ingresados
# -------------------------------------
print('\n\t--- DATOS INGRESADOS POR CONSOLA ---\t\n')
print(f'Nombre Usuario: {nombre_usuario}')
print(f'Edad Usuario: {edad_usuario}')
print(f'Tiene Trabajo?: {es_trabajador}')
print(f'Sueldo Usuario: {sueldo_usuario:.2f}')



