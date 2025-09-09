# -----------------------------
# Declaración Clase Empleado
# -----------------------------
class Empleado:
    # -----------------------------
    # Atributo de Clase
    # -----------------------------
    contador_empleados = 0

    # -----------------------------
    # Constructor
    # -----------------------------
    def __init__(self, nombre, departamento):
        # -----------------------------
        # Atributos de Instancia
        # -----------------------------
        self.nombre = nombre
        self.departamento = departamento

        # -----------------------------
        # Aumento del Contador
        # -----------------------------
        Empleado.contador_empleados += 1
        
        # -----------------------------
        # Asignar valor de Contador a la variable ID
        # -----------------------------
        self.id = Empleado.contador_empleados

    # -----------------------------
    # Método de Clase
    # -----------------------------
    @classmethod
    def obtener_total_empleados(cls):
        # print(f'[CLASSMETHOD] Contador: {cls.contador_empleados}') [Retorna el contador_personas de la clase]
        return cls.contador_empleados