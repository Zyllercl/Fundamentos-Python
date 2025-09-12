
# ----------------------
# Creación de Clase
# ----------------------
class Monitor:
    # ----------------------
    # Atributos de Clase
    # ----------------------
    contador_monitores = 0

    # ----------------------
    # Constructor
    # ----------------------
    def __init__(self, marca, tamano):
        # Aumento del contador
        Monitor.contador_monitores += 1

        # ----------------------
        # Atributos de Instancia
        # ----------------------
        self.id_monitor = Monitor.contador_monitores
        self.marca = marca
        self.tamano = tamano

    # Modificación del Método STR
    def __str__(self):
        mensaje = f'ID: {self.id_monitor} - Marca: {self.marca} - Tamaño: {self.tamano}'

        return mensaje

# ----------------------
# Pruebas
# ----------------------
if __name__ == '__main__':
    # Creación del Objeto tipo Monitor
    monitor_msi = Monitor('MSI', 24)
    print(monitor_msi)

    monitor_samsung = Monitor('Samsung', 27)
    print(monitor_samsung)