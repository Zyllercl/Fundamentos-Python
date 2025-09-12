from dispositivo_entrada import DispositivoEntrada

# ----------------------
# Creación de Clase
# ----------------------
class Teclado(DispositivoEntrada):
    # ----------------------
    # Atributos de Clase
    # ----------------------
    contador_teclados = 0

    # ----------------------
    # Constructor
    # ----------------------
    def __init__(self, marca, tipo_entrada):
        # Aumento del contador
        Teclado.contador_teclados += 1

        # ----------------------
        # Atributos de Instancia
        # ----------------------
        self.id_teclado = Teclado.contador_teclados

        # Inicialización de los Atributos de la Clase Dispositivos de Entrada
        super().__init__(marca, tipo_entrada)

    # Modificación del Método STR
    def __str__(self):
        mensaje = f'ID: {self.id_teclado} - Marca: {self.marca} - Tipo entrada: {self.tipo_entrada}'

        return mensaje

# ----------------------
# Pruebas
# ----------------------
if __name__ == '__main__':
    # Creación del objeto tipo Teclado
    teclado_razer = Teclado('Razer', 'USB')
    print(teclado_razer)

    teclaod_logitech = Teclado('Logitech', 'Wireless')
    print(teclaod_logitech)