#Librerias
import random
from statistics import mode, median, mean
# Actividades  
# 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, 
# deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”. 

edad = int(input("Ingrese su edad por favor: "))

if edad > 18:
    print("Es mayor de edad")
else:
    print("No sos mayor de edad")

# 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá 
# mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el 
# mensaje “Desaprobado”. 

nota = int(input("Ingrese su nota por favor: "))

if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

# 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un 
# número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso 
# contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del 
# operador de módulo (%) en Python para evaluar si un número es par o impar. 

num = int(input("Ingrese un numero par por favor: "))

if num % 2 == 0:
    print("Ha ingresado un numero par")
else:
    print("Por favor, ingrese un número par")

# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las 
# siguientes categorías pertenece: 
# ● Niño/a: menor de 12 años. 
# ● Adolescente: mayor o igual que 12 años y menor que 18 años. 
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. 
# ● Adulto/a: mayor o igual que 30 años.     

edadCategoria = int(input("Ingrese su edad por favor: "))

if edadCategoria < 12:
    print("Usted es un niño/a")
elif edadCategoria >=12 and edadCategoria < 18:
    print("Usted es un adolescente")
elif edadCategoria >= 18 and edadCategoria < 30:
    print("Usted es un adulto/a joven")
elif edadCategoria >= 30:
    print("Usted es un adulto/a")
else:
    print("Su edad no se encuentra dentro de las categorias establecidas")

# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres 
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en 
# pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por 
# pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso 
# de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal 
# como una lista o un string. 

contrasena = input("Ingrese su contraseña por favor: ")

if len(contrasena) >= 8 and len(contrasena) <= 14:
    print("Ha ingresado la contraseña correcta")
else:
    print("Por favor, ingrese una contraseña que tenga entre 8 y 14 caracteres")    

#6) Escribir un programa que tome la lista 
# numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si 
# hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla. 

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

print(f"Media: {media} Mediana: {mediana} Moda: {moda}")

if media > mediana and mediana > moda:
    print("Sesgo positivo o a la derecha")
elif media < mediana and mediana < moda:
    print("Sesgo negativo o a la izquierda")
else:
    print("Sin sesgo o simétrico")   

# 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado 
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por 
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por 
# pantalla. 

texto = input("Ingrese un texto por favor: ")
vocales = "aeiouAEIOU"

if texto[-1] in vocales:
    print(texto,"!") 
else:
     print(texto)

# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 
# dependiendo de la opción que desee: 
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. 
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro. 
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro. 
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el 
# usuario e imprimir el resultado por pantalla. 

nombre = input("Ingrese su nombre por favor: ")
opcion = int(input("Selecciona una opcion: 1) Mayuscula 2) Minuscula 3) Primera letra mayuscula: "))

match opcion:
    case 1:
        print(nombre.upper())
    case 2:
        print(nombre.lower())
    case 3:
        print(nombre.title())
    case _:
        print("Opcion no valida")

# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la 
# magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado 
# por pantalla: 

magnitudTerremoto = float(input("Ingrese la magnitud del terremoto por favor: "))

if magnitudTerremoto < 3.0:
    print("Muy leve. Imperceptible")
elif magnitudTerremoto >= 3.0 and magnitudTerremoto < 4.0:
    print("Leve. Ligeramente perceptible")
elif magnitudTerremoto >= 4.0 and magnitudTerremoto < 5.0:
    print("Moderado. Sentido por personas, pero generalmente no causa daños")
elif magnitudTerremoto >= 5.0 and magnitudTerremoto < 6.0:
    print("Fuerte. Puede causar daños en estructuras débiles")
elif magnitudTerremoto >= 6.0 and magnitudTerremoto < 7.0:
    print("Muy fuerte. Puede causar daños significativos")
elif magnitudTerremoto >= 7.0:
    print("Extremo. Puede causar daños graves a gran escala")
else:
    print("Magnitud no valida")

# 10)
# Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes 
# del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla 
# si el usuario se encuentra en otoño, invierno, primavera o verano.    

meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]

hemisferio = input("Ingrese el hemisferio en el que se encuentra (Norte o Sur): ")
hemisferio = hemisferio.lower()
mes = input("Ingrese el mes del año por favor: ")
mes = mes.lower()   
dia = int(input("Ingrese el dia del mes por favor: "))

if hemisferio == "norte":
    if (mes == "diciembre" and dia >= 21) or (mes == "enero") or (mes == "febrero") or (mes == "marzo" and dia <= 20):
        print("Usted se encuentra en invierno")
    elif (mes == "marzo" and dia >= 21) or (mes == "abril") or (mes == "mayo") or (mes == "junio" and dia <= 20):
        print("Usted se encuentra en primavera")
    elif (mes == "junio" and dia >= 21) or (mes == "julio") or (mes == "agosto") or (mes == "septiembre" and dia <= 20):
        print("Usted se encuentra en verano")
    elif (mes == "septiembre" and dia >= 21) or (mes == "octubre") or (mes == "noviembre") or (mes == "diciembre" and dia <= 20):
        print("Usted se encuentra en otoño")
    else:
        print("Fecha no valida")

elif hemisferio == "sur":
    if (mes == "diciembre" and dia >= 21) or (mes == "enero") or (mes == "febrero") or (mes == "marzo" and dia <= 20):
        print("Usted se encuentra en verano")
    elif (mes == "marzo" and dia >= 21) or (mes == "abril") or (mes == "mayo") or (mes == "junio" and dia <= 20):
        print("Usted se encuentra en otoño")
    elif (mes == "junio" and dia >= 21) or (mes == "julio") or (mes == "agosto") or (mes == "septiembre" and dia <= 20):
        print("Usted se encuentra en invierno")
    elif (mes == "septiembre" and dia >= 21) or (mes == "octubre") or (mes == "noviembre") or (mes == "diciembre" and dia <= 20):
        print("Usted se encuentra en primavera")
    else:
        print("Fecha no valida")
