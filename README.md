# UTN-TUPaD-Programacion1
Repositorio de la materia Programación I - UTN.

## TP 10, 11 y 12

| TP | Archivo principal | Explicación y ejemplos |
| --- | --- | --- |
| 10 - POO | [TP10_POO_CanelladaFacundo.py](<10 - Poo/TP10_POO_CanelladaFacundo.py>) | [Guía de estudio](<10 - Poo/GUIA_ESTUDIO.md>) |
| 11 - Acceso a Datos | [TP11_AccesoADatos_CanelladaFacundo.py](<11 - Acceso a Datos/TP11_AccesoADatos_CanelladaFacundo.py>) | [Guía de estudio](<11 - Acceso a Datos/GUIA_ESTUDIO.md>) |
| 12 - API REST | [TP12_APIRest_CanelladaFacundo.py](<12 - API Rest/TP12_APIRest_CanelladaFacundo.py>) y [app.py](<12 - API Rest/app.py>) | [Guía de estudio](<12 - API Rest/GUIA_ESTUDIO.md>) |

Las soluciones siguen los enunciados `TP POO.pdf`, `tp_grupal_accesodatos.pdf`
y `trabajo_practico_api_rest.pdf`, junto con sus respectivas guías teóricas.
Las clases se mantienen en archivos separados y los comentarios explican las
decisiones que conviene comprender para el examen.

### Preparación

Desde la raíz del repositorio, en PowerShell:

```powershell
python -m venv .venv
& ".\.venv\Scripts\python.exe" -m pip install -r ".\12 - API Rest\requirements.txt"
```

El entorno `.venv` ya fue creado durante la resolución. Los TP 10 y 11 utilizan
solo la biblioteca estándar de Python; el TP 12 requiere Flask y requests.
No es necesario activar el entorno si se usa su intérprete como en los ejemplos.

### Ejecución

```powershell
# Menú con los cinco ejercicios de POO.
& ".\.venv\Scripts\python.exe" ".\10 - Poo\TP10_POO_CanelladaFacundo.py"

# Demostración CRUD: crea la base, agrega ejemplos, modifica y elimina un libro.
& ".\.venv\Scripts\python.exe" ".\11 - Acceso a Datos\TP11_AccesoADatos_CanelladaFacundo.py"

# Inicia la API en http://127.0.0.1:5000. Se detiene con Ctrl+C.
& ".\.venv\Scripts\python.exe" ".\12 - API Rest\TP12_APIRest_CanelladaFacundo.py"
```

Con la API ejecutándose, abrir otra terminal en la raíz y ejecutar:

```powershell
& ".\.venv\Scripts\python.exe" ".\12 - API Rest\test_api.py"
```

El TP 12 importa el repositorio del TP 11 y usa el mismo archivo
`11 - Acceso a Datos/biblioteca.db`. Las rutas se calculan desde los archivos
Python: ejecutar desde otra carpeta no crea una base diferente por accidente.
Si la base no existe, se crea automáticamente. La demostración del TP 11 agrega
nuevos ejemplos cada vez que se ejecuta; no vacía los datos anteriores.

### Pruebas automáticas

```powershell
& ".\.venv\Scripts\python.exe" -m unittest discover -s ".\10 - Poo" -p "test_*.py" -v
& ".\.venv\Scripts\python.exe" -m unittest discover -s ".\11 - Acceso a Datos" -p "test_*.py" -v
& ".\.venv\Scripts\python.exe" -m unittest discover -s ".\12 - API Rest" -p "test_endpoints.py" -v
```

Las pruebas de datos y de API usan bases temporales. `test_endpoints.py` inicia
y detiene su propio servidor para comprobar también `test_api.py` con requests.
Los archivos generados (`.venv`, cachés y bases SQLite) están excluidos de Git.
