# 📂 Sobrecarga de Operadores en Python

---

## 📌 1. Sobrecarga de Operadores
> **Definición:**
> - La **Sobrecarga de Operadores** permite redefinir cómo funcionan los operadores `(+, -, *, ==, etc.)` cuando se aplican a objetos de clases personalizadas. Esto se logra implementando métodos especiales en la clase `(por ejemplo, __add__, __eq__, __mul__).`
> - La **Sobreescritura de la Sobrecargax de Operadores** sustituye la funcionalidad padre del operador, definiendo un nuevo comportamiento en la clase.

### 🔹 Operadores Aritméticos
Se utilizan para realizar operaciones matemáticas básicas entre objetos.

| Operador | Método Especial            | Descripción                            |
| -------- | -------------------------- | -------------------------------------- |
| `+`      | `__add__(self, otro)`      | Suma dos objetos                       |
| `-`      | `__sub__(self, otro)`      | Resta dos objetos                      |
| `*`      | `__mul__(self, otro)`      | Multiplica dos objetos                 |
| `/`      | `__truediv__(self, otro)`  | División normal                        |
| `//`     | `__floordiv__(self, otro)` | División entera (redondeo hacia abajo) |
| `%`      | `__mod__(self, otro)`      | Obtiene el módulo o residuo            |
| `**`     | `__pow__(self, otro)`      | Potencia                               |

### 🔹 Operadores de Comparación
Permiten comparar objetos y devolver valores booleanos.

| Operador | Método Especial      | Descripción       |
| -------- | -------------------- | ----------------- |
| `==`     | `__eq__(self, otro)` | Igual a           |
| `!=`     | `__ne__(self, otro)` | Distinto de       |
| `>`      | `__gt__(self, otro)` | Mayor que         |
| `<`      | `__lt__(self, otro)` | Menor que         |
| `>=`     | `__ge__(self, otro)` | Mayor o igual que |
| `<=`     | `__le__(self, otro)` | Menor o igual que |

### 🔹 Operadores de Asignación
Se usan para actualizar el valor de un objeto en combinación con operaciones aritméticas. 

| Operador | Método Especial             | Descripción            |
| -------- | --------------------------- | ---------------------- |
| `+=`     | `__iadd__(self, otro)`      | Suma y asigna          |
| `-=`     | `__isub__(self, otro)`      | Resta y asigna         |
| `*=`     | `__imul__(self, otro)`      | Multiplica y asigna    |
| `/=`     | `__itruediv__(self, otro)`  | Divide y asigna        |
| `//=`    | `__ifloordiv__(self, otro)` | Divide entero y asigna |
| `%=`     | `__imod__(self, otro)`      | Módulo y asigna        |
| `**=`    | `__ipow__(self, otro)`      | Potencia y asigna      |

### 🔹 Operadores Unarios
Operan sobre un sólo objeto, transformando su valor o representación.

| Operador | Método Especial    | Descripción                  |
| -------- | ------------------ | ---------------------------- |
| `-x`     | `__neg__(self)`    | Negativo (cambia el signo)   |
| `+x`     | `__pos__(self)`    | Positivo (mantiene el signo) |
| `~x`     | `__invert__(self)` | Complemento bit a bit        |
