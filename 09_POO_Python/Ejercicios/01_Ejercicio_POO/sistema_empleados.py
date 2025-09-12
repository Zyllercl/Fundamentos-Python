from empresa import Empresa
from empleado import Empleado

print(f'[~ Sistema de Empleados ~]\n')

# -----------------------------
# Creación de Instancia de una Empresa
# -----------------------------
empresa_kmv = Empresa('KMV')

# -----------------------------
# Agregando Nuevos Empleados a la empresa "KMV"
# -----------------------------
empresa_kmv.contratar_empleado('Pepe', 'Bordador')
empresa_kmv.contratar_empleado('Vladimir', 'Reponedor')
empresa_kmv.contratar_empleado('Albert', 'Bordador')
empresa_kmv.contratar_empleado('Fran', 'Técnico')

# -----------------------------
# Mostrando el Total de Objetos de tipo Empleado
# -----------------------------
print(f'[EMPLEADOS] Total: {Empleado.obtener_total_empleados()}\n')

# -----------------------------
# Consultar por Empleados por Departamento
# -----------------------------
departamento_especifico = "Bordador"
print(f'[DEPARTAMENTO] Total empleados en el departamento {departamento_especifico}: {empresa_kmv.empleados_por_departamento(departamento_especifico)}')

# -----------------------------
# Obtener Información Total de los Empleados
# -----------------------------
empresa_kmv.obtener_total_empleados()