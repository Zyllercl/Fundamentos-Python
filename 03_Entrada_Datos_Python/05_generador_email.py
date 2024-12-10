'''
    SISTEMA GENERADOR DE EMAILS

    Def:
        Crear un generador de email con los siguientes datos:
            
            Datos:
                - 'nombres'             -> 'Pedro Alejandro'
                - 'apellidos'           -> 'Perez Castillo'
                - 'extension correo'    -> 'gmail | yahoo | outlook'
                - 'extension dominio'   -> '.com | .es | .cl'
'''
print('-----\tGENERADOR DE EMAILS\t-----\n')

# Variables
nombre = input('Ingresa tus nombres: ')
apellido= input('Ingresa tus apellidos: ')
extension_correo = input('Extension correo (gmail | yahoo | outlook): ')
extension_dominio = input('Extension dominio (.com | .es | .cl): ')

nombre_email = nombre.strip().lower().replace(' ', '.')
apellido_email = apellido.strip().lower().replace(' ', '.')
extension_correo = extension_correo.strip().lower().replace(' ', '')
extension_dominio = extension_dominio.strip().lower().replace(' ', '')

print(f'----------\n')
print(f'Correo generado: {nombre_email}.{apellido_email}@{extension_correo}{extension_dominio}\n')

