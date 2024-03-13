import logging as log


""" 
    # Enviar la informacion a un archivo
        # Definicion de parametros:
            format=
            %(asctime)s:    -> Agrega el tiempo (Fecha y Hora) al mensaje de LOG
            %(levelname)s:  -> Agrega si fue DEBUG, INFO, WARNING, ERROR o CRITICAL
            %s(filename)s:  -> Agrega el nombre del archivo al mensaje del LOG
            %(lineno)s      -> Agrega el numero de linea al mensaje del LOG
            %(message)s     -> Muestra el mensaje que hemos agregado al LOG
            
            datefmt='%I:%M:%S %p' -> Formato de la hora (
                %I -> Hora
                %M -> Minutos
                %S -> Segundos
                %p -> HORA PM
            )
"""


# Configuracion de los LOGs
log.basicConfig(
    level=log.DEBUG,
    format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
    datefmt='%I:%M:%S %p',
    handlers= [
        # La INFO por consola se traspasa al archivo 'usuarios.log'
        log.FileHandler('log_base.log'),
        log.StreamHandler()
    ]
)


# TESTING #
if __name__ == '__main__':
    # Tipos de mensajes del LOG (Orden ASC)
    log.debug('[DEBUG] Mensaje a nivel DEBUG')
    log.info('[INFO] Mensaje a nivel INFO')
    log.warning('[WARNING] Mensaje a nivel WARNING')
    log.error('[ERROR] Mensaje a nivel ERROR')
    log.critical('[CRITICAL] Mensaje a nivel CRITICAL')