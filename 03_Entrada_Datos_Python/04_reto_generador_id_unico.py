'''
    SISTEMA GENERADOR DE ID ÚNICO

    Def:
        Con los datos ingresados el sistema deberá realizar lo siguiente:

            1.- Del valor 'nombre', usar sólo las 2 primeras letras y convertislas a mayúsculas.
            2.- Del valor 'apellido', usar las dos 2 primeras letras y convertirlas a mayúsculas.
            3.- Del valor 'año', usar los dos últimos dígitos.
        
        El sistema deberá generar un valor aleatorio de 4 dígitos utilizando la función randint.

        Con los datos obtenidos se debe generar un ID único de la siguiente forma:
            Ejemplo:
                - 'nombre'          -> 'Bellamy'    -> BE
                - 'apellido'        -> 'Blake'      -> BL
                - 'año'             -> 1987         -> 87
                - 'Valor Aleatorio' -> randint()    -> 1111
            
                Resultado ID único: BEBL871111
'''
import random

print('-----\tGENERADOR DE ID ÚNICO\t-----\n')

# Variables
nombre = input('Ingrese su nombre: ')
apellido= input('Ingrese su apellido: ')
anho_nacimiento = input('Ingrese su fecha de nacimiento (YYYY): ')
num_aleatorio = str(random.randint(0000,9999))

nombre_id = nombre.strip().upper()[0:2]             # Toma los dos primeros valores, 0 y 1 (No considera la posición 2)
apellido_id = apellido.strip().upper()[0:2]         # Toma los dos primeros valores, 0 y 1 (No considera la posición 2)
anho_nacimiento_id = anho_nacimiento.strip()[2:]    # Toma la posicion 2 hasta el final (4 posiciones máximo)

id_unico = f'{nombre_id}{apellido_id}{anho_nacimiento_id}{num_aleatorio}'

print(f'''
    Hola {nombre},
        Tu nuevo número de idenfiticación (ID) es el siguiente:
        {id_unico}
        Felicidades!
''')