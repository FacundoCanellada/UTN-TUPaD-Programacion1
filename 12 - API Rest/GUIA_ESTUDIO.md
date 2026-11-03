# TP 12: API REST de biblioteca con Flask y SQLite

Material utilizado: `trabajo_practico_api_rest.pdf` y `guia_api_rest.pdf`.
Este TP reutiliza los modelos, el repositorio y la base del TP 11.

## Archivos y responsabilidades

- `TP12_APIRest_CanelladaFacundo.py`: entrada que conserva el nombre de los TP del repositorio.
- `app.py`: aplicación Flask, rutas HTTP, validaciones y respuestas JSON.
- `repositorio_api.py`: permite importar el paquete `biblioteca` del TP 11.
- `requirements.txt`: dependencias Flask y requests.
- `test_api.py`: cliente HTTP que realiza la secuencia pedida con requests.
- `test_endpoints.py`: pruebas automáticas con bases temporales, incluyendo HTTP real.

La ruta de importación se calcula con `Path(__file__)` porque la carpeta del TP 11
tiene espacios y no puede usarse directamente como nombre de un paquete Python.
Se agrega esa carpeta a `sys.path` y se importa `biblioteca.repositorio`.
Se usa el código original y el archivo `11 - Acceso a Datos/biblioteca.db`.

## 1. Ejecutar y probar

Comandos desde la raíz del repositorio, en PowerShell:

```powershell
# Solo si todavía no existe el entorno.
python -m venv .venv

# Instalar dependencias.
& ".\.venv\Scripts\python.exe" -m pip install -r ".\12 - API Rest\requirements.txt"

# Opcional: cargar los ejemplos del TP 11 antes de iniciar Flask.
& ".\.venv\Scripts\python.exe" ".\11 - Acceso a Datos\TP11_AccesoADatos_CanelladaFacundo.py"

# Iniciar el servidor; esta terminal permanece ocupada hasta presionar Ctrl+C.
& ".\.venv\Scripts\python.exe" ".\12 - API Rest\TP12_APIRest_CanelladaFacundo.py"
```

También se puede iniciar ejecutando `12 - API Rest/app.py`.
No ejecutar ambas entradas a la vez: las dos inician la misma aplicación en el puerto 5000.
Abrir `http://127.0.0.1:5000/api/libros` en el navegador permite consultar el listado.
Si no se cargaron libros, la respuesta es `[]` con HTTP 200.

En una **segunda terminal**, también en la raíz:

```powershell
& ".\.venv\Scripts\python.exe" ".\12 - API Rest\test_api.py"
```

El servidor debe estar activo para ese script. Si se usa otro servidor o puerto,
se puede indicar `--url http://127.0.0.1:5001`.

## 2. Recorrido de una petición

```text
Cliente (requests o navegador)
    -> HTTP: método + URL + JSON opcional
    -> Flask selecciona una función por ruta y método
    -> La función valida datos y llama al repositorio
    -> El repositorio ejecuta SQL en biblioteca.db
    -> Flask devuelve JSON + código HTTP
```

`crear_app()` construye la aplicación y registra sus rutas.
El parámetro opcional `ruta_db` permite usar una base temporal en las pruebas.
`app = crear_app()` construye la aplicación normal, con la base compartida.
La inicialización crea tablas si faltan y conserva los datos existentes.

## 3. Endpoints

| Método | Ruta | Entrada | Éxito |
| --- | --- | --- | --- |
| GET | `/api/autores` | Sin cuerpo | Lista de autores, 200 |
| GET | `/api/autores/<id>` | ID en URL | Autor, 200; ruta adicional para consultar uno |
| POST | `/api/autores` | `nombre`, `nacionalidad` | Autor creado con ID, 201 |
| GET | `/api/libros` | Sin cuerpo | Lista con autor obtenido por JOIN, 200 |
| GET | `/api/libros/<id>` | ID en URL | Libro con autor, 200 |
| POST | `/api/libros` | `titulo`, `anio`, `autor_id` | Libro creado, 201 |
| PUT | `/api/libros/<id>` | Uno o más campos del libro | Libro actualizado, 200 |
| DELETE | `/api/libros/<id>` | ID en URL | Confirmación de eliminación, 200 |

Ejemplo de alta de autor:

```json
{"nombre": "Jorge Luis Borges", "nacionalidad": "Argentina"}
```

Si la respuesta indica que su ID es 1, un alta de libro puede enviar:

```json
{"titulo": "Ficciones", "anio": 1944, "autor_id": 1}
```

El ID debe ser el que realmente devuelva la creación del autor.
La respuesta del libro tiene esta estructura:

```json
{
  "id": 1,
  "titulo": "Ficciones",
  "anio": 1944,
  "autor_id": 1,
  "autor": {"id": 1, "nombre": "Jorge Luis Borges", "nacionalidad": "Argentina"}
}
```

## 4. Resolución de las rutas, paso a paso

### GET

1. El decorador `@app.route(..., methods=["GET"])` asocia la URL con una función.
2. Para un listado se llama a `obtener_libros_db()` u `obtener_autores_db()`.
3. Para un detalle se llama al método que recibe el ID.
4. Si el detalle devuelve `None`, se responde 404.
5. `jsonify()` convierte listas y diccionarios a una respuesta JSON.

### POST

1. `request.get_json()` permite leer el cuerpo enviado por el cliente.
2. `leer_json()` exige un objeto no vacío y rechaza campos desconocidos.
3. Las funciones `validar_*` comprueban los campos obligatorios y sus tipos.
4. Antes de insertar un libro, se verifica que exista su autor.
5. El repositorio inserta, confirma con `commit()` y consulta el registro creado.
6. Se devuelve el registro completo con su ID y HTTP 201.

### PUT

1. Se busca el libro. Si no existe, se devuelve 404.
2. Se lee el JSON con los campos a modificar.
3. `datos.get("titulo", libro["titulo"])` toma el título nuevo o conserva el anterior.
4. Se hace lo mismo con año y autor y se validan los valores resultantes.
5. Se comprueba que el autor exista y se ejecuta el `UPDATE`.
6. Se consulta y devuelve el libro actualizado con HTTP 200.

La guía describe PUT como reemplazo completo y en su ejemplo conserva los campos
omitidos. El enunciado pide enviar los campos a modificar; se siguió esa indicación
para poder enviar solo `{"titulo": "Nuevo título"}`. Un valor explícito `null`
no cuenta como campo omitido: se rechaza con HTTP 400.

### DELETE

1. Se recibe el ID en la URL.
2. Se ejecuta `DELETE ... WHERE id = ?`.
3. Si no se eliminó ninguna fila, se devuelve 404.
4. Si se eliminó, se devuelve `{"mensaje": "Libro eliminado correctamente.", "id": 1}` y HTTP 200.

## 5. Validaciones y códigos

- **200:** consulta, actualización o eliminación correcta.
- **201:** autor o libro creado.
- **400:** falta un campo obligatorio, JSON inválido, texto vacío, tipo incorrecto,
  cuerpo que no es un objeto, campo desconocido o PUT vacío.
- **404:** libro inexistente, autor inexistente o ruta desconocida.
- **405:** método HTTP no permitido para la ruta.

Los textos se recortan con `strip()`; los años e IDs deben ser enteros positivos.
No se acepta `"1944"` como año porque es una cadena. Tampoco se acepta `true`:
en Python los booleanos son una subclase de `int`, por eso se verifica el tipo exacto.
Los errores devuelven un objeto JSON con la clave `error`, por ejemplo:

```json
{"error": "Libro no encontrado."}
```

## 6. Secuencia de test_api.py

1. `GET /api/libros`: exige 200 y muestra cuántos libros había.
2. `POST /api/autores`: exige 201 y guarda el ID recibido.
3. `POST /api/libros`: usa ese ID y exige 201.
4. `PUT /api/libros/<id>`: cambia solo el título y exige 200.
5. `GET /api/libros/<id>`: comprueba el título guardado y que se conservó el año.
6. `DELETE /api/libros/<id>`: exige 200 y comprueba el ID y el mensaje de confirmación.
7. Otro `GET` de ese libro debe devolver 404.

Las peticiones llevan `timeout=5` para que una conexión no espere indefinidamente.
El libro de prueba se elimina y el autor de prueba queda registrado, porque el
enunciado no solicita un endpoint para borrar autores. Ejecutar el script modifica
la misma base que la API esté utilizando.

## Para el examen

Flask atiende las peticiones en el servidor y requests las envía desde el cliente.
JSON es el formato de intercambio: no es una tabla ni una base de datos.
El código HTTP indica el resultado y el cuerpo JSON contiene datos o una explicación.
El repositorio convierte esa operación en SQL y SQLite conserva los cambios.

Preguntas para practicar: ¿qué diferencia hay entre 200 y 201?, ¿por qué GET no
debe insertar libros?, ¿por qué crear el autor primero?, ¿cómo se conserva un campo
omitido en PUT?, ¿qué diferencia hay entre 400 y 404?, ¿por qué la API usa JOIN?
