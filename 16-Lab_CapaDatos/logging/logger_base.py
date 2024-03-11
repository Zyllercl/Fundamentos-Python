import logging as log

""" 
    # DEFINICION:
    El registro (logging | LOG ) es una forma de registrar mensajes en diferentes niveles de severidad durante la ejecución de un programa. Un controlador de flujo es una forma de manejar estos registros y determinar dónde se envían. Por ejemplo, los controladores de flujo pueden enviar registros a la consola, a un archivo, a través de una red, etc.
"""

# Configuracion basica del manejo de logging (INFO POR CONSOLA)

# log.basicConfig(level=log.DEBUG) # Se mostrara el mensaje DEBUG en adelante
# log.basicConfig(level=log.WARNING) # Se mostrara el mensaje WARNING en adelante

# Enviar la informacion a un archivo
""" 
    # DEFINICIONES DE PARAMETROS
        format=
        '
        %(asctime)s:    -> Agrega el tiempo (Fecha y Hora) al mensaje de LOG
        %(levelname)s:  -> Agrega si fue DEBUG, INFO, WARNING, ERROR o CRITICAL
        %s(filename)s:  -> Agrega el nombre del archivo al mensaje del LOG
        %(lineno)s      -> Agrega el numero de linea al mensaje del LOG
        %(message)s     -> Muestra el mensaje que hemos agregado al LOG
        '
        
        datefmt='%I:%M:%S %p' -> Formato de la hora (
            %I -> Hora
            %M -> Minutos
            %S -> Segundos
            %p -> HORA PM
        )
"""

log.basicConfig(level=log.DEBUG,
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt='%I:%M:%S %p',
                handlers = [
                    log.FileHandler('capa_datos.log'), # Se agrega la INFO de consola al archivo
                    log.StreamHandler()
                ])

if __name__ == '__main__':
    # Tipos de mensajes (orden ASC)
    log.debug('[DEGUB] Mensaje a nivel DEBUG')
    log.info('[INFO] Mensaje a nivel INFO')
    log.warning('[WARNING] Mensaje a nivel WARNING')
    log.error('[ERROR] Mensaje a nivel ERROR')
    log.critical('[CRITICAL] Mensaje a nivel CRITICAL')