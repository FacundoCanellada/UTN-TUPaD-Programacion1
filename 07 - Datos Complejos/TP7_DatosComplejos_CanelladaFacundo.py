# # 1) Dado el diccionario precios_frutas 
# # Añadir las siguientes frutas con sus respectivos precios: 
# # ● Naranja = 1200 
# # ● Manzana = 1500 
# # ● Pera = 2300 
# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 
# 1450} 
# print(f"Precios de las frutas: ", precios_frutas)

# precios_frutas.update({"Naranja": 1200, "Manzana": 1500, "Pera": 2300})
# print(f"Precios de las frutas actualizado: ", precios_frutas)

# # 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
# # desarrollado en el punto anterior, actualizar los precios de las siguientes frutas: 
# # ● Banana = 1330 
# # ● Manzana = 1700 
# # ● Melón = 2800 
# precios_frutas.update({"Banana": 1330, "Manzana": 1700, "Melón": 2800})
# print(f"Precio de frutas modificado", precios_frutas)

# # 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
# # desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los 
# # precios. 
# claves_frutas = list(precios_frutas.keys())
# print(f"Listado de las frutas sin precio: ", claves_frutas)

# 4) Escribí un programa que permita almacenar y consultar números telefónicos. 
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor. 
# • Luego, pedí un nombre y mostrale el número asociado, si existe.
registro_usuarios = {}

print("--- REGISTRO DE 5 USUARIOS ---\n")

for i in range(5):
    print(f"Usuario {i + 1} de 5:")
    
    nombre = input("Ingresa el nombre: ").strip()
    numero = input(f"Ingresa el numero de {nombre}: ").strip()
    
    registro_usuarios[nombre] = numero
    print(f"{nombre} registrado con éxito")

print("--- Todos los usuarios registrados ---")
for nombre, correo in registro_usuarios.items():
    print(f"{nombre}: {correo}")

# 5) Solicita al usuario una frase e imprime: 
# • Las palabras únicas (usando un set). 
# • Un diccionario con la cantidad de veces que aparece cada palabra. 

frase = input("Ingresa una frase: ").strip().lower()

palabras = frase.split()

palabras_unicas = set(palabras)
print(f"Palabras únicas: {palabras_unicas}")

frecuencia = {}
for pal in palabras:
    if pal in frecuencia:
        frecuencia[pal] += 1
    else:
        frecuencia[pal] = 1

print(f"Frecuencia de palabras: {frecuencia}")

# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. 
# Luego, mostrá el promedio de cada alumno. 

alumnos = {}

for i in range(3):
    nombre = input(f"Nombre del alumno {i+1}: ").strip()
    
    nota1 = float(input("  Nota 1: "))
    nota2 = float(input("  Nota 2: "))
    nota3 = float(input("  Nota 3: "))
    
    alumnos[nombre] = (nota1, nota2, nota3)

print("Promedios")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / 3
    print(f"{nombre}: Promedio = {promedio:.2f}")

# 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 
# y Parcial 2: 
# • Mostrá los que aprobaron ambos parciales. 
# • Mostrá los que aprobaron solo uno de los dos. 
# • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

parcial1 = {"Ana", "Luis", "Carlos", "Marta"}
parcial2 = {"Carlos", "Marta", "Juan", "Pedro"}

print(f"Aprobaron Parcial 1: {parcial1}")
print(f"Aprobaron Parcial 2: {parcial2}\n")

ambos = parcial1.intersection(parcial2)
print(f"Aprobaron ambos parciales: {ambos}")

solo_uno = parcial1.symmetric_difference(parcial2)
print(f"Aprobaron solo un parcial: {solo_uno}")

total = parcial1.union(parcial2)
print(f"Total de estudiantes aprobados (sin repetir): {total}")

# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. 
# Permití al usuario: 
# • Consultar el stock de un producto ingresado. 
# • Agregar unidades al stock si el producto ya existe. 
# • Agregar un nuevo producto si no existe.

inventario = {
    "manzanas": 50,
    "yerba": 20,
    "leche": 15
}

print("--- SISTEMA DE STOCK ---")
producto = input("Ingresa el nombre del producto: ").strip().lower()

if producto in inventario:
    print(f"El producto '{producto}' existe. Stock actual: {inventario[producto]} unidades.")
    cantidad = int(input(f"¿Cuántas unidades deseas agregar al stock de {producto}?: "))
    inventario[producto] += cantidad
    print(f"Stock actualizado. Ahora hay {inventario[producto]} unidades.")
else:
    print(f"El producto '{producto}' no está registrado.")
    cantidad = int(input(f"Ingresa el stock inicial para {producto}: "))
    inventario[producto] = cantidad
    print(f"¡Producto '{producto}' registrado con éxito!")

print("Inventario final:", inventario)
# 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos. 
# Permití consultar qué actividad hay en cierto día y hora. 
agenda = {
    ("lunes", "09:00"): "Clase de Programación 1",
    ("miercoles", "14:00"): "Práctica en Laboratorio",
    ("viernes", "11:00"): "Entrega de Trabajo Práctico"
}

print("--- CONSULTA DE AGENDA ---")
dia_consulta = input("Ingresa el día a consultar (ej: lunes): ").strip().lower()
hora_consulta = input("Ingresa la hora a consultar (ej: 09:00): ").strip()

busqueda = (dia_consulta, hora_consulta)

if busqueda in agenda:
    print(f"\nActividad encontrada: {agenda[busqueda]}")
else:
    print("\nNo hay actividades programadas para ese día y hora.")

# 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo 
# diccionario donde: 
# • Las capitales sean las claves. 
# • Los países sean los valores. 

paises_capitales = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Uruguay": "Montevideo",
    "Brasil": "Brasilia"
}

capitales_paises = {}

for pais, capital in paises_capitales.items():
    capitales_paises[capital] = pais

print("Diccionario original (País: Capital):")
print(paises_capitales)

print("\nNuevo diccionario invertido (Capital: País):")
print(capitales_paises)
