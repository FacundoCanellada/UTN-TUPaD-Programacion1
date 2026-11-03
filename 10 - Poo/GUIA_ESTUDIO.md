
# TP 10: Programación Orientada a Objetos

Material utilizado: `TP POO.pdf` y `POO - Python.pdf`.
Ejecutar `TP10_POO_CanelladaFacundo.py` desde la carpeta raíz, como indica
el README. Elegir entre 1 y 5; cada ejercicio vuelve al menú al finalizar.
Los ejercicios 1 a 4 son interactivos y el 5 contiene una demostración con objetos.
Los datos de este TP viven en memoria y se pierden al cerrar el programa.

## Antes de empezar

- **Clase:** define los atributos y los métodos de un tipo de objeto.
- **Instancia u objeto:** un ejemplar concreto, por ejemplo `Alumno("Ana", 1)`.
- **`__init__`:** inicializa los atributos al crear la instancia.
- **`self`:** el objeto sobre el que se está trabajando.
- **Atributo:** un dato del objeto, por ejemplo `alumno.legajo`.
- **Método:** una función de la clase, como `alumno.calcular_promedio()`.
- **Asociación:** un objeto guarda referencias a otros, como un alumno con notas.
- **`__str__`:** determina el texto que se obtiene al hacer `print(objeto)`.

Cada lista está creada dentro de `__init__`. Así, dos alumnos tienen listas de
notas independientes. Una lista definida directamente en la clase se compartiría
entre instancias, lo que sería un error para estos ejercicios.

Las relaciones de este TP son del tipo «tiene»: una matriz tiene celdas,
un alumno tiene notas, un plato tiene ingredientes y un barrio tiene viviendas.
Se pasan objetos ya creados a los métodos `agregar_*`; esto sigue el enfoque
de agregación presentado por la guía. No se necesita herencia para resolverlos.
Una lista de objetos, por sí sola, no determina su ciclo de vida.

## 1. Matriz y celdas

Archivos: `ejercicio_1_matriz/celda.py`, `matriz.py` y `carga_matriz.py`.

1. `Celda` guarda `fila`, `columna` y `valor`.
2. `Matriz` crea su lista `celdasMatriz`.
3. Se pide primero el valor. Si es `FIN`, se termina sin pedir coordenadas.
4. Para otro valor se piden fila y columna y se crea una `Celda`.
5. `buscar_celda()` recorre la lista y compara **fila y columna juntas**.
6. `agregar_celda()` rechaza una posición ocupada; el valor anterior se conserva.
7. Se muestran las celdas y se permite consultar posiciones con `obtener_valor()`.

Ejemplo: cargar `hola` en `(0, 1)` y `mundo` en `(1, 1)` es válido.
Volver a cargar `(0, 1)` produce un mensaje de duplicado. Consultar `(9, 9)`
devuelve el mensaje exacto solicitado por el enunciado.

Es una representación por lista de celdas: no se reserva una tabla rectangular
completa. Para cargar y consultar elegimos coordenadas enteras desde 0.

## 2. Alumnos y notas

Archivos: `ejercicio_2_notas/nota.py`, `alumno.py` y `carga_notas.py`.

1. `CargaNotas.main()` crea la lista `alumnos`.
2. Se pide nombre y legajo y se crea un `Alumno` con su lista `notas` vacía.
3. Se pide una cátedra y una nota, se crea `Nota` y se agrega al alumno.
4. Recién después se pregunta si se desea otra nota. Esto obliga a cargar una.
5. Al terminar las notas, se agrega el alumno a la lista general.
6. Se repite la carga si se desea otro alumno.
7. Se recorren alumnos y notas y se muestra `calcular_promedio()`.

El promedio se calcula con `suma de notas / cantidad de notas`. Para 8 y 9,5:
`(8 + 9.5) / 2 = 8.75`. Se retorna el resultado y la interfaz lo imprime.
El método también lanza `ValueError` si se lo llama sin notas, evitando dividir
por cero. Se aceptan notas decimales no negativas; el enunciado no fija una escala.

`@staticmethod` permite llamar `CargaNotas.main()` sin crear un objeto de carga;
no necesita `self` porque trabaja con variables locales.

## 3. Menú del restaurante

Archivos: `ejercicio_3_restaurante/ingrediente.py`, `plato.py` y `menu_restaurant.py`.

1. Se crea la lista `platosMenu`.
2. Se pide nombre, precio y si el elemento es bebida.
3. Si `esBebida` es `True`, se omite la carga de ingredientes.
4. Para una comida se carga al menos un `Ingrediente` con nombre, cantidad y unidad.
5. Se pregunta si se desea otro ingrediente y luego otro plato.
6. Se valida el plato y se lo agrega al menú.
7. Se imprime nombre y precio; para comidas se imprime además la tabla de ingredientes.

Ejemplo: Pizza, $450, no es bebida; Queso, 300, gramos. Luego Agua, $100,
es bebida: no se pide ingrediente. `validar_ingredientes()` también permite
comprobar la regla si se construyen los objetos desde código.

## 4. Costo de computadoras

Archivos: `ejercicio_4_computadoras/componente_cpu.py`, `computadora.py`
y `costo_computadora.py`.

1. Se crea una `Computadora` con marca, modelo y lista de componentes.
2. Se carga al menos un `ComponenteCPU` con nombre, marca, cantidad y precio unitario.
3. Cada subtotal es `cantidad * precio`.
4. `calcular_costo()` suma los subtotales.
5. `calcular_precio_venta()` agrega el recargo correspondiente.
6. Se muestra el detalle y se pregunta si se desea cotizar otra computadora.
7. Si se responde SI se crea una computadora nueva, con una lista vacía.

Ejemplo del PDF: `16000 + 20000 + 2 * 8000 + 7500 = 59500`.
Corresponde 30%: `59500 + 17850 = 77350`.

Para costo menor a $50.000 se usa 40%. El enunciado no define la igualdad:
se decidió aplicar **30% desde $50.000 inclusive**, dejando documentado el criterio.
Se usan `float` y formato de dos decimales para seguir el nivel introductorio;
el formato de pantalla no convierte internamente los cálculos a decimales exactos.

## 5. Barrio, viviendas y habitaciones

Archivos: `ejercicio_5_barrio/habitacion.py`, `vivienda.py`, `barrio.py`
y `demostracion_barrio.py`.

1. Se crean habitaciones con sus metros cuadrados.
2. Se asocian las habitaciones con sus viviendas.
3. Se asocian las viviendas con el barrio.
4. `getSuperficieTotalTerreno()` suma los terrenos de todas las viviendas.
5. `getSuperficieTotalTerrenoXManzana(manzana)` suma solo los de esa manzana.
6. `getMetrosCuadradosCubiertos()` suma las habitaciones de una vivienda.
7. Si la suma supera el terreno, lanza la excepción solicitada. Igualar el terreno es válido.
8. `getSuperficieTotalCubierta()` suma las superficies cubiertas llamando al método anterior.

La demostración tiene terrenos de 200 y 150 m²: total 350 m².
Las habitaciones suman `30 + 20 = 50` y `25 + 15 = 40`: total cubierto 90 m².
Una vivienda separada, con 20 m² de terreno y una habitación de 25 m²,
demuestra la excepción y su captura con `try/except`.

## Validaciones y repaso

`entrada.py` centraliza los reintentos de teclado: texto no vacío, enteros,
decimales finitos, cantidades positivas y respuestas SI/NO. Para decimales
se admite punto o coma. Los modelos contienen las reglas específicas del ejercicio.
Se conservaron nombres de atributos y métodos de la consigna, aunque algunos
usan mayúsculas internas en lugar del estilo habitual `snake_case` de Python.

Preguntas para practicar:

1. ¿Qué diferencia hay entre crear una clase y crear un objeto?
2. ¿Por qué las listas se inicializan dentro de `__init__`?
3. ¿Por qué se usa `and` al buscar la posición de una celda?
4. ¿Cómo garantizan los bucles al menos una nota o un ingrediente?
5. ¿Qué diferencia hay entre `return` y `print`?
6. ¿Por qué se reutiliza el cálculo de una vivienda desde el barrio?
7. ¿Qué ocurre al lanzar `ValueError` y qué hace `except`?

Las comprobaciones se encuentran en `test_poo.py` y se ejecutan con el comando
del README. Para estudiar, leer primero las clases y después los métodos de carga.
