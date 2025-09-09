from empleado import Empleado

# -----------------------------
# Declaración Clase Empresa
# -----------------------------
class Empresa:
    # -----------------------------
    # Constructor
    # -----------------------------
    def __init__(self, nombre):
        # -----------------------------
        # Atributos de Instancia
        # -----------------------------
        self.nombre = nombre
        self.empleados = []
    
    # -----------------------------
    # Método Crear un Empleado
    # -----------------------------
    def contratar_empleado(self, nombre, departamento):
        # -----------------------------
        # Definición variable "Empleado" como Objeto
        # -----------------------------
        empleado = Empleado(nombre, departamento)

        # -----------------------------
        # Agregando al Nuevo Empleado a la lista
        # -----------------------------
        self.empleados.append(empleado)

    # -----------------------------
    # Método Obtener Empleado por Departamento
    # -----------------------------
    def empleados_por_departamento(self, departamento):
        # -----------------------------
        # Variable Local
        # -----------------------------
        contador_empleados_por_departamento = 0

        # -----------------------------
        # Iterando sobre la lista "Empleados"
        # -----------------------------
        for empleado in self.empleados:
            if empleado.departamento == departamento:
                contador_empleados_por_departamento += 1
        return contador_empleados_por_departamento
    
    # -----------------------------
    # Método Obetner Total Empleados por Empresa
    # -----------------------------
    def obtener_total_empleados(self):
        print(f'\n[{self.nombre}] Información Empleados')

        for empleado in self.empleados:
            print(f'ID: {empleado.id} , Nombre: {empleado.nombre}\t, Departamento: {empleado.departamento}')
