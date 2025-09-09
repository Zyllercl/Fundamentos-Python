# 📂 Programación Orientada a Objetos (POO) en Python

---

## 📌 1. Fundamentos de POO
> **Definición:**
> - Python es un lenguaje Orientado a Objetos donde cada objeto es una representación de una entidad real en nuestro programa.
> - Para crear un objeto, primero necesitamos definir una Clase (**Class**) que actúa como plantilla.
> - Una clase representa las características comunes de los objetos, siendo una abstracción de los mismos.


### 🔹 Analogía
- Si necesitamos construir un edificio:
- La **Clase** es el plano (plantilla)
- Los **Objetos** son los edificios construidos basados en ese plano

### 🔹 Elementos de una Clase
| Elemento    | Descripción                                    |
|-------------|------------------------------------------------|
| Atributos   | Características o propiedades de los objetos   |
| Métodos     | Acciones que pueden realizar los objetos. Estas acciones son funciones, pero cuando se asocian con una 'Clase' se les denomina 'métodos'    |

### 🔹 Conceptos Clave
| Concepto        | Definición                                      | Ejemplo en Python                                 |
|-----------------|-------------------------------------------------|---------------------------------------------------|
| **Clase**       | Plantilla para crear objetos                    | `class Persona:`                                  |
| **Objeto**      | Instancia (ejemplar) de una clase               | `p1 = Persona()`                                  |
| **Atributos**   | Características o propiedades del objeto        | `self.nombre = "Ana"`                             |
| **Métodos**     | Funciones asociadas a una clase                 | `def saludar(self): print("Hola")`                |
| **Instanciación** | Proceso de crear un objeto a partir de una clase | `persona1 = Persona()`                         |

### 🔹 Estructura Básica
```python
class Persona:
    # Atributos
    nombre
    apellido
    email
    celular

    # Métodos
    agregar_nombre()
    mostrar_apellido()
```

### 🔹 Instanciación
- Crear objetos a partir de una clase se llama `"Instanciar una Clase"`

**Ejemplo:**
```python
# Objeto 1
persona1.nombre = "Jhon"
persona1.apellido = "Reyes"

# Objeto 2
persona2.nombre = "Bellamy"
persona2.apellido = "Blake"
```

---

## 📌 2. Constructores
> **Definición:**
> - Un constructor es un **'Método especial'** que se utiliza para **crear un objeto o instanciar una clase.**
> - Se utiliza para crear e inicializar los atributos de un nuevo objeto.

### 🔹 Sintaxis del Constructor
```python
class NombreDeLaClase:
    def __init__(self, parametro1, parametro2):
        self.parametro1 = parametro1
        self.parametro2 = parametro2
```

### 🔹 Elementos del Constructor
| Elemento     | Descripción                                    |
|--------------|------------------------------------------------|
| `__init__()` | Método inicializador (tipo dunder - doble underscore) |
| `self`       | Referencia al objeto actual en memoria         |

### 🔹 Dirección de Memoria
- Cuando se crea un objeto, este ocupa un espacio en memoria (ej: 0x311...).
- La variable `self` referencia al objeto actual con el que se interactúa.
- Para obtener la dirección de memoria:

```python
# Formato decimal
id(variable)

# Formato hexadecimal
hex(id(variable))
```

---

## 📌 3. Encapsulamiento
> **Definición:**
> - El **encapsulamiento** es un principio de POO que consiste en **ocultar la información que almacena un objeto**, conocido como **Estado del Objeto**.
> - Permite proteger los datos de una clase para que no sean modificados directamente desde fuera.

### 🔹 Tipos de Encapsulamiento
| Modificador | Sintaxis | Descripción |
|-------------|----------|-------------|
| Público | `nombre` | Accesible desde cualquier parte del código |
| Protegido | `_nombre` | Accesible sólo desde la clase y sus subclases. **NO se puede alterar el valor de la variable.** |
| Privado | `__nombre` | Accesible sólo desde dentro de la clase |

### 🔹 Niveles de Protección de Atributos
| Tipo | Sintaxis | Descripción |
|------|----------|-------------|
| Protegido | `self._nombre` | Un guion bajo. Indica que no debería accederse desde fuera de la clase |
| Privado | `self.__nombre` | Doble guion bajo. Solo puede accederse desde dentro de la clase |

> **Nota**: En Python, la protección es por convención. El guion bajo es una señal para otros desarrolladores de cómo deberían usarse los atributos.

### 🔹 Métodos y Decoradores
| Método | Definición | Decorador |
|--------|------------|-----------|
| GET | Obtener/recuperar información de una variable | `@property` |
| SET | Modificar/cambiar información de una variable | `@nombre.setter` |

> **Nota**: Los decoradores permiten modificar el comportamiento de los métodos:
> - `@property`: Convierte un método en un atributo de sólo lectura
> - `@nombre.setter`: Permite modificar el valor del atributo protegido

`Notas importantes:`
- Los métodos GET y SET solo son necesarios para acceder a atributos desde fuera de la clase.
- No se debe modificar directamente atributos protegidos o privados desde fuera de la clase.
- Para crear atributos de **sólo lectura** (read only), se omite el **método setter**.

### 🔹 Ejemplo de los Métodos GET y SET [BÁSICO]
```python
class Persona:
    def __init__(self):
        self.__nombre = ''  # Atributo privado
    
    # Getter
    def get_nombre(self):
        return self.__nombre
    
    # Setter
    def set_nombre(self, nombre):
        self.__nombre = nombre
```

### 🔹 Ejemplo de los Métodos GET y SET [RECOMENDADO]
```python
class Persona:
    def __init__(self):
        self._nombre = ''  # Atributo protegido
    
    # -----------------------
    # Decorador @property: Es una propiedad de la Clase.
    # ----------------------- 
    @property
    def nombre(self):
        return self._nombre
    
    # -----------------------
    # Decorador @{atributo}.setter: Es una propiedad de la Clase, consiste en cambiar un atributo dentro de una clase.
    # ----------------------- 
    @nombre.setter
    def set_nombre(self, nombre):
        self._nombre = nombre
```

### 🔹 Beneficios del Encapsulamiento
- Protección de datos.
- Control de acceso.
- Mantenimiento más sencillo.
- Modificación de implementación sin afectar el código.

---

## 📌 4. Atributos de Clases
> **Definición:**
> Los atributos en Python pueden ser de dos tipos: **atributos de clase** y **atributos de instancia**, cada uno con su propio alcance y forma de acceso.

### 🔹 Tipos de Atributos

| Tipo | Descripción | Acceso |
|------|-------------|---------|
| Atributos de Clase | Se definen fuera de los métodos y se comparten entre todos los objetos | Directamente desde la clase |
| Atributos de Instancia | Se definen dentro de los métodos y son específicos de cada objeto | A través de un objeto |

### 🔹 Ejemplo de Implementación
```python
class Persona:
# Atributo de clase
atributo_clase = 0

def __init__(self, atributo_instancia):
    # Atributo de instancia
    self.atributo_instancia = atributo_instancia
```

### 🔹 Características Importantes
- Los atributos de clase se comparten entre todas las instancias.
- Un objeto puede acceder a los atributos de clase (aunque no es recomendado).
- Los atributos de instancia son únicos para cada objeto.
- Los atributos de clase se definen fuera de cualquier método.

> **Nota**: Se recomienda acceder a los atributos de clase usando el nombre de la clase (Ej: `Persona.atributo_clase`) en lugar de hacerlo a través de una instancia.

---

## 📌 5. Métodos de Clase
> **Definición:**
> - Son funciones que se definen dentro de una clase y están diseñadas para trabajar con los atributos y objetos de dicha clase.

### 🔹 Tipos de Métodos

| Tipo | Descripción | Decorador |
|------|-------------|-----------|
| Método Estático | No recibe argumentos implícitos y no puede modificar el estado de la clase | `@staticmethod` |
| Método Clase | Tiene acceso y puede modificar el estado de la clase, esto se aplicará a todas las instancias (objetos) de la clase | `@classmethod` |
| Método de Instancia | Recibe `self` como parametro. Puede acceder y modificar atributos de instancia y de clase. | X |

### 🔹 Características
- Los **Métodos de Clase** pueden modificar el estado que afectará a todas las instancias
- Se puede acceder a variables de clase mediante un objeto (Contexto Dinámico a Estático), pero NO se puede acceder de forma viceversa

### 🔹 Ejemplo de Implementación
```python
class Persona:
    contador_personas = 0  # Variable de clase

    @staticmethod
    def get_contador_estatico():
        return Persona.contador_personas

    @classmethod
    def get_contador_clase(cls):
        return cls.contador_personas
```

**Nota**: Se recomienda usar `@classmethod` cuando se necesita acceder o modificar atributos de clase, ya que proporciona una referencia a la clase mediante el parámetro **cls**

---

## 📌 6. Herencia
> **Definición:**
> - La **Herencia** en Python es un mecanismo de la **POO** que permite que una **clase hija** (o **subclase**) herede atributos y métodos de otra **clase padre** (o **superclase**).
> - Permite reutilizar código y expandir de funcionalidades sin duplicar la lógica.

### 🔹 Conceptos Clave en Herencia

| Concepto            | Descripción |
|---------------------|-------------|
| **Clase Padre**     | También llamada **superclase**: proporciona atributos y métodos que la clase hija puede reutilizar. |
| **Clase Hija**      | También llamada **subclase**: hereda de la clase padre y puede extender o modificar sus comportamientos. |
| **Herencia Simple** | La clase hija hereda de una única clase padre. |
| **Herencia Múltiple** | La clase hija hereda de más de una clase padre. |
| **Sobrescritura (Override)** | Cuando una clase hija redefine un método heredado de la clase padre para cambiar su comportamiento. |
| **`super()`**       | Permite invocar métodos de la clase padre desde la clase hija sin referirse directamente al nombre de la clase padre. |

---

## 📌 7. Polimorfismo
> **Definición:**
> - El **Polimorfismo** permite que objetos de diferentes clases respondan de forma distinta a la **misma llamada de método o función**. Esto promueve la flexibilidad, mantenibilidad y reutilización del código.

###  🔹 Conceptos Clave en Polimorfismo

| Concepto                       | Descripción |
|--------------------------------|-------------|
| **Polimorfismo**               | Capacidad de que una misma interfaz (método, función u operador) se comporte de forma distinta según la clase del objeto que lo utiliza. ||
| **Duck Typing**                | En Python, si un objeto tiene el método esperado, se considera compatible sin importar su tipo concreto. |
| **Polimorfismo con Operadores** | Operadores como `+`, `len()` u otros métodos mágicos (`__add__`, etc.) pueden comportarse diferente según el tipo de objeto. |
