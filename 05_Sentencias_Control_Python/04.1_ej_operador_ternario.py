'''
    APLICACION DE SALUD Y FITNESS

    Def:
        - Crear una aplicación que solicite lo siguiente:
            1.- Nombre de usuario
            2.- Pasos caminados en el día
        
        - Además se deberá definir las siguientes constantes:
            # CONSTANTES:
                - META_PASOS_DIARIO = 10000
                - CALORIAS_POR_PASO = 0.04 # Valor aproximado en kilocalorias
        
            Para calcular las calorias quemadas se debe ocupar la siguiente formula:
                - calorias_quemadas = pasos_diarios * CALORIAS_POR_PASO
            
            Y se verifica si se cumplió a meta de pasos diarios con la siguiente formua:
                - meta_alcanzada = pasos_diarios >= META_PASOS_DIARIO
'''

print(f'-----   APLICACION DE SALUD Y FITNESS   -----')
# Variables
META_PASOS_DIARIO = 10000
CALORIAS_POR_PASO = 0.04

nombre_usuario = input('Ingrese su nombre: ')
pasos_diarios = int(input('Cuantos pasos has caminado hoy?: '))

calorias_quemadas = pasos_diarios * CALORIAS_POR_PASO
meta_alcanzada = pasos_diarios >= META_PASOS_DIARIO
meta_alcanzada = "Si" if meta_alcanzada else "No"

print(f'''\nINFORMACIÓN FITNESS\n
Usuario: {nombre_usuario}
N° Pasos: {pasos_diarios}
Calorias quemadas: {calorias_quemadas} Kcal
Pasos diarios alcanzados: {meta_alcanzada}
Meta de pasos diario: {META_PASOS_DIARIO}\n
''')
