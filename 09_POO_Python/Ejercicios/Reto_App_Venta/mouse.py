from dispositivo_entrada import DispositivoEntrada

# ----------------------
# Creación de Clase
# ----------------------
class Mouse(DispositivoEntrada):
    # ----------------------
    # Atributos de Clase
    # ----------------------
    contador_ratones = 0
    
    # ----------------------
    # Constructor
    # ----------------------
    def __init__(self, marca, tipo_entrada):
        # Aumento del contador
        Mouse.contador_ratones += 1
        
        # ----------------------
        # Atributos de Instancia
        # ----------------------
        self.id_raton = Mouse.contador_ratones

        # Inicialización de los Atributos de Clase [Forma 1]
        # self.marca = marca
        # self.tipo_entrada = tipo_entrada

        # Inicialización de los Atributos de Clase [Forma 2 - RECOMENDADA]
        super().__init__(marca, tipo_entrada)

    # Modificación del Método STR
    def __str__(self):
        mensaje = f'ID: {self.id_raton} - Marca: {self.marca} - Tipo entrada: {self.tipo_entrada}'

        return mensaje

# ----------------------
# Pruebas
# ----------------------
if __name__ == '__main__':
    # Creación del objeto tipo Raton
    mouse_razer = Mouse('Razer', 'USB')
    print(mouse_razer)

    mouse_logitech = Mouse('Logitech', 'Wireless')
    print(mouse_logitech)


