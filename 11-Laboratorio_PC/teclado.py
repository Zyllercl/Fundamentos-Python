from dispositivo_entrada import DispositivoEntrada

class Teclado(DispositivoEntrada):
    # Variables Globales
    contador_teclados = 0
    
    # Metodos
    def __init__(self, marca, tipo_entrada):
        # Aumentamos el contador
        Teclado.contador_teclados += 1
        # Atributos
        self._id_teclado = Teclado.contador_teclados # Seteamos la ID con el contador
        super().__init__(marca, tipo_entrada) # Herencia de los atributos Padre
    
    def __str__(self):
        return f'ID: {self._id_teclado}, Marca: {self._marca}, Tipo_entrada: {self._tipo_entrada}'
    
    
if __name__ == '__main__':
    print('[!] Testeando clase Teclado...')
    teclado_hp = Teclado('Logitech', 'Bluetooth')
    print(teclado_hp)
    teclado_acer = Teclado('Acer', 'USB')
    print(teclado_acer)