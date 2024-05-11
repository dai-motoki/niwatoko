Traducción al español:

# niwatoko v1.1.4
# niwatoko v1.1.4

El lenguaje de programación Niwatoko ahora proporciona la función de importación de módulos (¡la primera en el mundo*).
El lenguaje de programación Niwatoko ahora proporciona la función de importación de módulos (¡la primera en el mundo*).
Ahora se puede procesar archivos Markdown con variables generados por el generador de indicaciones de Anthropic en Niwatoko.
Ahora se puede procesar archivos Markdown con variables generados por el generador de indicaciones de Anthropic en Niwatoko.


## Contenido de la actualización
## Contenido de la actualización

### Adición de la función de importación (cita)
### Adición de la función de importación (cita)
- Ahora se puede citar el contenido de otros archivos dentro de un archivo Markdown.
- Ahora se puede citar el contenido de otros archivos dentro de un archivo Markdown.
- Esto mejora la reutilización del código y facilita la gestión de la documentación.
- Esto mejora la reutilización del código y facilita la gestión de la documentación.

- El método de cita es el siguiente:
- El método de cita es el siguiente:
   ```markdown
   ```markdown
   - `variable` = extensión [./ruta_del_archivo(sin_extensión)]
   - `variable` = extensión [./ruta_del_archivo(sin_extensión)]
   - `variable` = [./ruta_del_archivo]
   - `variable` = [./ruta_del_archivo]
   ```
   ```
- Ejemplo:
- Ejemplo:
   ```markdown
   ```markdown
    `hello.py` = py [./hello]
    `hello.py` = py [./hello]
    `hello.py` = [./hello.py]
    `hello.py` = [./hello.py]
   ```
   ```
- Esta función es la primera en el mundo.
- Esta función es la primera en el mundo.
- Tenga en cuenta que la extensión del archivo (.py) debe estar incluida entre corchetes [].
- Tenga en cuenta que la extensión del archivo (.py) debe estar incluida entre corchetes [].

### Adición de la función de variable de documentación
### Adición de la función de variable de documentación
```
```
- Ahora se pueden definir variables {{variable}} dentro de un archivo Markdown y hacer referencia a ellas en otros lugares.
```
```
- Ahora se pueden definir variables {{variable}} dentro de un archivo Markdown y hacer referencia a ellas en otros lugares.
  - Por ejemplo, si escribe `{{variable}}`, se cargará el archivo `variable.md` del mismo nivel.
```
```
  - Por ejemplo, si escribe `{{variable}}`, se cargará el archivo `variable.md` del mismo nivel.
- Esto mejora la legibilidad y el mantenimiento de la documentación.
- Esto mejora la legibilidad y el mantenimiento de la documentación.

## Instalación
## Instalación
```
```

Para más detalles, consulte el siguiente URL:
Para más detalles, consulte el siguiente URL:
[https://niwatoko2.vercel.app/installation.html](https://niwatoko2.vercel.app/installation.html)

1. Si ya tiene Python y la clave de Anthropic configurados, puede usar el siguiente comando:
1. Si ya tiene Python y la clave de Anthropic configurados, puede usar el siguiente comando:

   ```
   ```
   pip install niwatoko
   pip install niwatoko
   ```
   ```

   O para actualizar a la última versión, ejecute el siguiente comando:
   O para actualizar a la última versión, ejecute el siguiente comando:

   ```
   ```
   pip install --upgrade niwatoko
   pip install --upgrade niwatoko
   ```
   ```

## Ejercicio
## Ejercicio

Siga estos pasos:
Siga estos pasos:
- Preparación
- Preparación
1. Clone la rama principal de este repositorio.
1. Clone la rama principal de este repositorio.

   ```
   ```
   git clone -b main https://github.com/dai-motoki/niwatoko.git
   git clone -b main https://github.com/dai-motoki/niwatoko.git
   ```
   ```

2. Navegue al directorio clonado.
2. Navegue al directorio clonado.

   ```
   ```
   cd niwatoko/tests/test_docs/test_niwatoko_v1.1.3
   cd niwatoko/tests/test_docs/test_niwatoko_v1.1.3
   ```
   ```

- Ejecución
- Ejecución

1. Prepare el archivo `test_input.md`. Este archivo contiene el contenido de entrada que desea probar.
1. Prepare el archivo `test_input.md`. Este archivo contiene el contenido de entrada que desea probar.

```test_input.md
```test_input.md
## Citas
## Citas
- `addition_py` = py [./test_import_module_add]
- `addition_py` = py [./test_import_module_add]
```py
```
- `multiplication_py` = py [./test_import_module_multiple]  
- `multiplication_py` = py [./test_import_module_multiple]  
```py
```

## TODO
## TODO
Convierta `addition_py` y `multiplication_py` a un documento de especificación de requisitos solo en japonés.
Convierta `addition_py` y `multiplication_py` a un documento de especificación de requisitos solo en japonés.
También describa las pruebas necesarias.
También describa las pruebas necesarias.
```
```

2. Ejecute el siguiente comando para convertir el contenido de `test_input.md` y generar el archivo `output.md`:
2. Ejecute el siguiente comando para convertir el contenido de `test_input.md` y generar el archivo `output.md`:

   ```
   ```
   niwatoko test_input.md -o output.md
   niwatoko test_input.md -o output.md
   ```
   ```

3. Ejecute el siguiente comando para convertir el contenido de `output.md` a código Python y generar el archivo `output.py`:
3. Ejecute el siguiente comando para convertir el contenido de `output.md` a código Python y generar el archivo `output.py`:

   ```
   ```
   niwatoko output.md -o output.py
   niwatoko output.md -o output.py
   ```
   ```

4. Revise el contenido de los archivos `output.md` y `output.py` generados y verifique que la salida sea la esperada.
4. Revise el contenido de los archivos `output.md` y `output.py` generados y verifique que la salida sea la esperada.

5. Repita la ejecución hasta que obtenga la salida esperada.
5. Repita la ejecución hasta que obtenga la salida esperada.