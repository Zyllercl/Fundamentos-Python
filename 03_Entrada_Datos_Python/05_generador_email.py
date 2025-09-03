"""
SISTEMA GENERADOR DE EMAILS
===========================

Definición:
-----------
Crear un generador de email con los siguientes datos:
    
    Datos de entradas:
        - 'nombres'             -> 'Pedro Alejandro'
        - 'apellidos'           -> 'Perez Castillo'
        - 'extension correo'    -> 'gmail | yahoo | outlook'
        - 'extension dominio'   -> '.com | .es | .cl'

Funcionamiento:
---------------
1. Los nombres y apellidos se transforman a minúsculas.
2. Los espacios se reemplazan por puntos (`.`).
3. Se concatenan nombre, apellido, extensión de correo y dominio
   para formar la dirección final.
"""


print('-----\tGENERADOR DE EMAILS\t-----\n')

# ------------------------------
# Entrada de datos
# ------------------------------
nombre = input('Ingresa tus nombres: ')
apellido= input('Ingresa tus apellidos: ')
extension_correo = input('Extension correo (gmail | yahoo | outlook): ')
extension_dominio = input('Extension dominio (.com | .es | .cl): ')

# Limpieza y formato del nombre y apellido
nombre_email = nombre.strip().lower().replace(' ', '.')
apellido_email = apellido.strip().lower().replace(' ', '.')

# Limpieza y formato de las extensiones
extension_correo = extension_correo.strip().lower().replace(' ', '')
extension_dominio = extension_dominio.strip().lower().replace(' ', '')

# Generación del correo final
correo_final = f"{nombre_email}.{apellido_email}@{extension_correo}{extension_dominio}"

# ------------------------------
# Salida de datos
# ------------------------------
print(f'\nCorreo generado automáticamente: {correo_final}\n')