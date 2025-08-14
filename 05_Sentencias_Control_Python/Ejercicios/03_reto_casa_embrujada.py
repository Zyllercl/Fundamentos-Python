'''
    CASA EMBRUJADA

    Def:
        - Nos encontramos en fantasilandia y se necesita un programa para saber si el usuario puede ingresar a la casa embrujada. Se deben cumplir las algunas de las siguientes condiciones para poder entrar al juego:
            
            1.- Debe tener más de 10 años
            2.- No debe darle miedo la oscuridad
'''

print(f'-----   CASA EMBRUJADA   -----') 
# Variables
edad = int(input('Ingrese su edad: '))
fobia_oscuridad = input('Le tienes miedo a la oscuridad? (Si/No): ')

fobia_oscuridad = (fobia_oscuridad.strip().lower() == 'si')

# si fobia_oscuridad es TRUE (Respuesta: Si) entonces entrada en el else.
if not fobia_oscuridad and edad >= 10:
    print('El usuario puede ingresar a la Casa Embrujada')
else:
    print('El usuario NO puede ingresar a la Casa Embrujada...')
