# Actividades
# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
print("Hola Mundo!")
# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
# el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
# por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
# realizar la impresión por pantalla.
nombre = input("Hola, por favor ingresa tu nombre: ")
print(f"Hola {nombre}!")
# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
# imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
# “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
# años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
# la impresión por pantalla.
nombre = input("Hola, por favor ingresa tu nombre: ")
apellido = input("Ahora ingresa tu apellido: ")
edad = int(input("A continuación ingresa tu edad: "))
lugar_residencia = input("Por último, ingresa tu lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar_residencia}.")
# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
# su perímetro.
radio = float(input("Ingrese el radio del círculo: "))
area = 3.1416 * radio ** 2
perimetro = 2 * 3.1416 * radio
print(f"El área del círculo es: {area}")
print(f"El perímetro del círculo es: {perimetro}")
# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
# cuántas horas equivale
segundos = int(input("Ingrese el número en segundos: "))
hora = segundos / 3600
print(f"El numero de segundos {segundos} equivale a {hora} horas.")
# 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
# multiplicar de dicho número.
numero = int(input("Ingrese el número de la tabla de multiplicar que quiera saber: "))
numero1 = numero * 1
numero2 = numero * 2    
numero3 = numero * 3
numero4 = numero * 4
numero5 = numero * 5
numero6 = numero * 6
numero7 = numero * 7
numero8 = numero * 8
numero9 = numero * 9
numero10 = numero * 10
print(f"{numero} x 1 = {numero1}")
print(f"{numero} x 2 = {numero2}")
print(f"{numero} x 3 = {numero3}")
print(f"{numero} x 4 = {numero4}")
print(f"{numero} x 5 = {numero5}")
print(f"{numero} x 6 = {numero6}")
print(f"{numero} x 7 = {numero7}")
print(f"{numero} x 8 = {numero8}")
print(f"{numero} x 9 = {numero9}")
print(f"{numero} x 10 = {numero10}")
# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
# pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
numeroEntero = int(input("Ingrese un número entero distinto de 0: "))
numeroEntero2 = int(input("Ingrese un segundo número entero distinto de 0: "))
suma = numeroEntero + numeroEntero2
resta = numeroEntero - numeroEntero2
multiplicacion = numeroEntero * numeroEntero2
division = numeroEntero / numeroEntero2
print(f"La suma de los números es: {suma}, la resta es: {resta}, la multiplicación es: {multiplicacion} y la división es: {division}.")
# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
# de masa corporal. 
peso = float(input("Ingrese su peso en kilos por favor: "))
altura = float(input("Ahora ingrese su altura: "))
imc = peso / (altura ** 2)
print(f"Su indice de masa corporal es: {imc}")
# 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
# pantalla su equivalente en grados Fahrenheit
gradosCelsius = float(input("Ingrese la temperatura en grados Celsius: "))
gradosFahrenheit = (gradosCelsius * 9/5) + 32
print(f"{gradosCelsius} grados Celsius equivalen a {gradosFahrenheit} grados Fahrenheit.")
# 10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
# dichos números
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
numero3 = float(input("Ingrese el tercer número: "))
promedio = (numero1 + numero2 + numero3) / 3
print(f"El promedio de los números ingresados es: {promedio}")