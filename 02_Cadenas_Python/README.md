# 📂 Cadenas en Python

---

## 📌 1. Cadenas
> **Definición:**
> - Una **cadena** o *string* es un tipo de dato que almacena una secuencia de caracteres.
> - En Python, las cadenas se encierran entre **comillas dobles** (`" "`) o **comillas simples** (`' '`).
> - Los caracteres pueden ser letras, números, símbolos o espacios.

**Ejemplo:**
```python
texto_1 = "Hola Mundo"
texto_2 = 'Python es lo mejor'
```

### 📌 1.1 Detalles de un String
> - Los caracteres de una cadena están **indexados** de manera secuencial.
> - Esto permite acceder a cada caracter indicando su **índice** (posición).
> - Los índices comienzan en `0` y pueden ser **negativos** (`-1` es el último caracter)

| Operación     | Resultado      |
|---------------|----------------|
| **string[0]**     | `Primer caracter` |
| **string[-1]**    | `Último caracter` |
| **string[0:5]**   | `Caracteres de íncide 0 al 4` |

**Ejemplo:**
```python
frase = "Obteniendo un caracter"

print(frase[0])     # 'O' -> primer caracter
print(frase[-1])    # 'r' -> último caracter
print(frase[0:5])   # 'Obten -> caracteres del índice 0 al 4
```

### 📌 1.2 Inmutabilidad de un String
> **Definición:**
> - En Python, las cadenas son **inmutables**, no se pueden modificar sus caracteres directamente.
> - Si se quiere cambiar, hay que **crear una nueva cadena**.

**Ejemplo:**
```python
frase = "Hola Mundo"
frase[0] = "h" # ❌ Error: 'str' object does not support item assignment
```