Traducción al español:

# niwatoko v1.1.3

Hemos reproducido la función de variable de documento de Anthropic como el segundo proyecto de código abierto más grande del mundo* y hemos proporcionado la función de importación de módulos (primera del mundo*).

## Contenido de la actualización

### Adición de la función de importación (cita)
- Ahora puede citar el contenido de otros archivos dentro de los archivos Markdown.
- Esto mejora la reutilización del código y facilita la gestión de la documentación.

- El método de cita es el siguiente:
   ```markdown
   - `nombre_variable` = extensión [./ruta_archivo(sin_extensión)]
   - `nombre_variable` = [./ruta_archivo.extensión]
   ```
- Ejemplo:
   ```markdown
    `hello.py` = py [./hello]
    `hello.py` = [./hello.py]
   ```
- Esta función es la primera de su tipo en el mundo.
- Tenga en cuenta que la extensión del archivo (.py) debe estar incluida entre corchetes [].

### Adición de la función de variable de documento
- Ahora puede definir variables dentro de los archivos Markdown y hacer referencia a ellas en otros lugares.
- Esto mejora la legibilidad y el mantenimiento de la documentación.
- Esta función es la segunda implementación en el mundo después de Anthropic.

## Instalación

Para más detalles, consulte el siguiente enlace:
[https://niwatoko2.vercel.app/installation.html](https://niwatoko2.vercel.app/installation.html)


1. Si ya tiene Python y la clave de Anthropic configurados, puede usar el siguiente comando:

   ```
   pip install niwatoko
   ```

   O para actualizar a la última versión, ejecute el siguiente comando:
   
   ```
   pip install --upgrade niwatoko
   ```


## Ejercicio

Siga estos pasos:
- Preparación
1. Clona la rama principal de este repositorio.

   ```
   git clone -b main https://github.com/dai-motoki/niwatoko.git
   ```

2. Navega al directorio clonado.

   ```
   cd niwatoko/tests/test_docs/test_niwatoko_v1.1.3
   ```

- Ejecución

1. Prepara el archivo `test_input.md`. Este archivo contiene el contenido de entrada que deseas probar.

```test_input.md
## Citas
- `addition_py` = py [./test_import_module_add]
```py
def add(a, b):
    """
    Función para sumar dos números

    Parámetros:
    a (int o float): Primer número
    b (int o float): Segundo número

    Devuelve:
    int o float: Suma de a y b
    """
    return a + b

def add_list(numbers):
    """
    Función para calcular la suma de una lista de números

    Parámetros:
    numbers (list): Lista de números

    Devuelve:
    int o float: Suma de los números
    """
    total = 0
    for num in numbers:
        total = add(total, num)
    return total

def add_multiple(*args):
    """
    Función para sumar múltiples números

    Parámetros:
    *args: Argumentos de longitud variable. Acepta cualquier número de valores numéricos

    Devuelve:
    int o float: Suma de los argumentos pasados
    """
    return add_list(args)
```
- `multiplication_py` = py [./test_import_module_multiple]  
```py
def multiply(a, b):
    """
    Función para multiplicar dos números

    Parámetros:
    a (int o float): Primer número
    b (int o float): Segundo número

    Devuelve:
    int o float: Producto de a y b
    """
    return a * b

def multiply_list(numbers):
    """
    Función para calcular el producto de una lista de números

    Parámetros:
    numbers (list): Lista de números

    Devuelve:
    int o float: Producto de los números
    """
    total = 1
    for num in numbers:
        total = multiply(total, num)
    return total


def multiply_multiple(*args):
    """
    Función para multiplicar múltiples números

    Parámetros:
    *args: Argumentos de longitud variable. Acepta cualquier número de valores numéricos

    Devuelve:
    int o float: Producto de los argumentos pasados
    """
    return multiply_list(args)```

## TODO
Convierta `addition_py` y `multiplication_py` en especificaciones de requisitos solo en japonés.
También describa las pruebas necesarias.
```

2. Ejecuta el siguiente comando para convertir el contenido de `test_input.md` y generar el archivo `output.md`:

   ```
   niwatoko test_input.md -o output.md
   ```

3. Ejecuta el siguiente comando para convertir el contenido de `output.md` a código Python y generar el archivo `output.py`:

   ```
   niwatoko output.md -o output.py
   ```

4. Revisa el contenido de los archivos `output.md` y `output.py` generados para verificar que la salida sea la esperada.

5. Repite los pasos anteriores hasta que obtengas la salida deseada.