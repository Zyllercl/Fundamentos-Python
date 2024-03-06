from dispositivo_entrada import DispositivoEntrada

class Mouse(DispositivoEntrada):
    # Variables Globales
    contador_mouses = 0
    
    # Metodos
    def __init__(self, marca, tipo_entrada):
        # Aumentamos el contador
        Mouse.contador_mouses += 1
        # Atributos
        self._id_raton = Mouse.contador_mouses # Seteamos la ID con el contador
        super().__init__(marca, tipo_entrada) # Herencia de los atributos Padre
    
    def __str__(self):
        return f'ID: {self._id_raton}, Marca: {self._marca}, Tipo_entrada: {self._tipo_entrada}'
    
    
if __name__ == '__main__':
    print('[!] Testeando clase Mouse...')
    mouse_hp = Mouse('HP', 'Cabble')
    print(mouse_hp)
    mouse_acer = Mouse('Acer', 'USB')
    print(mouse_acer)