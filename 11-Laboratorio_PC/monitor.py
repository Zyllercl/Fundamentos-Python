
class Monitor:
    # Variables Globales
    contador_monitores = 0
    
    def __init__(self, marca, tamanho):
        # Aumentamos el contador
        Monitor.contador_monitores += 1
        # Atributos
        self._id_monitor = Monitor.contador_monitores # Seteamos la ID con el contador
        self._marca = marca
        self._tamanho = tamanho
    
    def __str__(self):
        return f'ID: {self._id_monitor}, Marca: {self._marca}, Tamaño: {self._tamanho} Pulgadas'
    
    
if __name__ == '__main__':
    print('[!] Testeando clase Monitor...')
    monitor_samsung = Monitor('Samsung', 24)
    print(monitor_samsung)
    monitor_LG = Monitor('LG', 32)
    print(monitor_LG)