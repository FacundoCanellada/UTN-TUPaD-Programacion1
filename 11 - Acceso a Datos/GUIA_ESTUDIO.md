# TP 11: Biblioteca con POO y SQLite

Material utilizado: `tp_grupal_accesodatos.pdf` y `Guia_acceso_datos_Python.pdf`.
La entrada principal es `TP11_AccesoADatos_CanelladaFacundo.py`.
No necesita instalar librerías externas: `sqlite3` forma parte de Python.

## 1. Modelos de objetos

`biblioteca/autor.py` define `Autor(id_autor, nombre, nacionalidad)`.
`biblioteca/libro.py` define `Libro(id_libro, titulo, anio_publicacion, autor)`.
Ambos tienen `__init__` y `__str__`.

El atributo `libro.autor` guarda un objeto `Autor`, no solo un nombre.
Es una agregación: se crea el autor antes y se lo pasa al libro; un autor
puede estar asociado con varios libros. No se trata de herencia.

## 2. Base de datos y tablas

`biblioteca/repositorio.py` contiene `RepositorioBiblioteca`.
Su método `inicializar()` crea `biblioteca.db` y las tablas, si aún no existen:

```text
autores                          libros
id (PK autoincremental) <-------- autor_id (FK)
nombre                           id (PK autoincremental)
nacionalidad                     titulo
                                 anio
```

La PK identifica cada registro. La FK expresa a qué autor pertenece un libro.
Es una relación 1:N: un autor puede tener muchos libros y cada libro tiene un autor.
`NOT NULL` impide omitir esos datos. `PRAGMA foreign_keys = ON` activa
la verificación de la relación en cada conexión SQLite.

La ruta de la base se calcula desde el archivo del repositorio y queda en
`11 - Acceso a Datos/biblioteca.db`, aunque se ejecute Python desde otra carpeta.
`inicializar_db.py` permite crear solo las tablas, sin cargar ejemplos.

## 3. Flujo de una operación

1. `sqlite3.connect()` abre una conexión con el archivo SQLite.
2. `conexion.execute()` ejecuta SQL y devuelve un cursor.
3. Se usan `?` y una tupla para pasar valores por separado de la sentencia.
4. En una escritura, `commit()` confirma los cambios.
5. `closing()` cierra la conexión al salir del bloque, incluso ante errores.

Se usan conexiones breves por operación. `with conexion:` administra transacciones,
pero no cierra por sí solo la conexión; por eso aquí se usa `contextlib.closing`
y se deja `commit()` explícito, como en la guía.

Ejemplo:

```python
cursor = conexion.execute(
    "INSERT INTO autores (nombre, nacionalidad) VALUES (?, ?)",
    (nombre, nacionalidad),
)
conexion.commit()
id_generado = cursor.lastrowid
```

Los parámetros evitan que el texto ingresado se interprete como código SQL.
Nunca se arma una sentencia SQL concatenando títulos o nombres.

## 4. CRUD del enunciado

| Método | SQL | Resultado |
| --- | --- | --- |
| `registrar_autor(nombre, nacionalidad)` | `INSERT` | ID generado |
| `registrar_libro(titulo, anio, autor_id)` | `INSERT` | ID generado |
| `listar_libros()` | `SELECT` con `JOIN` | Lista de objetos `Libro`, cada uno con su `Autor` |
| `actualizar_titulo_libro(id_libro, nuevo_titulo)` | `UPDATE ... WHERE id = ?` | `True` si se encontró el registro |
| `eliminar_libro(id_libro)` | `DELETE ... WHERE id = ?` | `True` si se eliminó el registro |

`WHERE` limita la actualización o la baja al ID solicitado.
Omitirlo afectaría todos los registros de la tabla.
`cursor.rowcount` permite saber si la operación encontró una fila.

## 5. Cómo funciona el JOIN

```sql
SELECT libros.id, libros.titulo, libros.anio, libros.autor_id,
       autores.nombre AS autor_nombre,
       autores.nacionalidad AS autor_nacionalidad
FROM libros
JOIN autores ON libros.autor_id = autores.id
```

Por cada libro, se busca el autor cuyo `id` coincide con `autor_id`.
Así se obtiene el nombre sin repetirlo físicamente en cada fila de `libros`.
`AS` pone un nombre al dato devuelto. `sqlite3.Row` permite leerlo como
`fila["autor_nombre"]` en lugar de memorizar una posición numérica.

`fetchall()` recupera todas las filas; `fetchone()` recupera una o devuelve `None`.
La consulta ordena los listados por ID para que la salida sea predecible.

## 6. Prueba integral, paso a paso

Al ejecutar el archivo principal:

1. Se inicializa la base sin borrar datos existentes.
2. Se registran Borges y Allende y se guardan los IDs devueltos por SQLite.
3. Se registran Ficciones, El Aleph y La casa de los espíritus usando esos IDs.
4. Se muestra el listado con información del autor obtenida mediante `JOIN`.
5. Se actualiza Ficciones y se vuelve a consultar ese registro para comprobar el cambio.
6. Se elimina La casa de los espíritus y se muestra el listado final.

Con una base inicialmente vacía quedan dos autores y dos libros.
Cada ejecución vuelve a agregar los ejemplos, sin limpiar registros anteriores.
No se suponen IDs fijos, de modo que la secuencia también funciona si ya había datos.

## 7. Reutilización por el TP 12

Los métodos terminados en `_db` ofrecen las operaciones pedidas por el TP de API.
Devuelven diccionarios con tipos simples, que Flask puede convertir a JSON.
Por ejemplo, `insertar_autor_db()` reutiliza `registrar_autor()` y consulta el registro
creado. `listar_libros()` convierte los resultados de consulta a objetos del modelo.
El SQL permanece en este repositorio; la API se ocupa de HTTP y validaciones de entrada.

## Para el examen

- Memoria temporal: una lista desaparece al cerrar el programa.
- Persistencia: un `commit()` deja los cambios guardados en `biblioteca.db`.
- `lastrowid`: ID de la fila recién insertada.
- `(id_libro,)`: tupla de un elemento; la coma es necesaria.
- `JOIN`: combina información de tablas relacionadas.
- Una consulta que no encuentra datos devuelve `None` o una lista vacía.
- Una FK inválida produce `sqlite3.IntegrityError`; no guarda un libro huérfano.

`test_acceso_datos.py` verifica la secuencia CRUD, persistencia al reabrir la base,
claves foráneas, nombres con apóstrofes y consultas parametrizadas. Usa una base temporal.
