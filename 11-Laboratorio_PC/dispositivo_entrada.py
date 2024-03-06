
class DispositivoEntrada:
    # Inicializador
    def __init__(self, marca, tipo_entrada ):
        self._marca = marca
        self._tipo_entrada = tipo_entrada
        
    def __str__(self):
        print(f'Tipo de marca: {self._tipo_entrada}, marca: {self._marca}')
    
    """ # Metodos GET | SET
    @property
    def get_tipo_entrada(self):
        print('[+] Obteniendo tipo de entrada...')
        return self._tipo_entrada
    
    @get_tipo_entrada.setter
    def set_tipo_entrada(self, tipo_entrada):
        print('[-] Cambiando tipo de entrada...')
        self._tipo_entrada = tipo_entrada
        
    @property
    def get_marca(self):
        print('[+] Obteniendo marca...')
        return self._marca
    
    @get_marca.setter
    def set_marca(self, marca):
        print('[-] Cambiando marca...')
        self._marca = marca """
        
        
if __name__ == '__main__':
    print('[!] Testeando Dispositivo Entrada...')
    dispositivo = DispositivoEntrada('Cable', 'HP')
    dispositivo.__str__()