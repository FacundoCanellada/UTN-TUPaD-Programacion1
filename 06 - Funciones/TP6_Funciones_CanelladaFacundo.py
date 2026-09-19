import math
# 1. Crear una función llamada imprimir_hola_mundo que imprima por
# pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
# programa principal.
def imprimir_hola_mundo():
    print(f"Hola Mundo!")

imprimir_hola_mundo()

# 2. Crear una función llamada saludar_usuario(nombre) que reciba
# como parámetro un nombre y devuelva un saludo personalizado.
# Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá de
# volver: “Hola Marcos!”. Llamar a esta función desde el programa
# principal solicitando el nombre al usuario.
def saludar_usuario(nombre):
    print(f"Hola {nombre}")

nombre = input("Buenos días! Ingrese su nombre: ") 

saludar_usuario(nombre)
# 3. Crear una función llamada informacion_personal(nombre, apellido,
# edad, residencia) que reciba cuatro parámetros e imprima: “Soy
# [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pe
# dir los datos al usuario y llamar a esta función con los valores in
# gresados 
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre}, {apellido}, tengo {edad} años y vivo en {residencia}")

nombre = input("Buenos días! Ingrese su nombre: ")
apellido = input("Ahora su apellido: ") 
edad = int(input("Ahora su edad: "))  
residencia = input("Por último su lugar de residencia: ") 

informacion_personal(nombre, apellido, edad, residencia)
# 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el ra
# dio como parámetro y devuelva el área del círculo. calcular_peri
# metro_circulo(radio) que reciba el radio como parámetro y devuel
# va el perímetro del círculo. Solicitar el radio al usuario y llamar am
# bas funciones para mostrar los resultados.
def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

radio = float(input("Por favor ingrese el radio para calcular el area y el perimetro de un circulo: "))

area = calcular_area_circulo(radio) 
perimetro = calcular_perimetro_circulo(radio)

print(f"El área es: {area} y el perímetro: {perimetro}")
# 5. Crear una función llamada segundos_a_horas(segundos) que reciba
# una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y mos
# trar el resultado usando esta función.
def segundos_a_hora(segundos):
    return segundos / 3600

segundos = int(input("Ingrese la cantidad de segundos que quiere pasar a horas: "))
horas = segundos_a_hora(segundos)

print(f"La cantidad de segundos son {horas}, horas")
# 6. Crear una función llamada tabla_multiplicar(numero) que reciba un
# número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la función.
def tabla_multiplicar(numero): 
    for i in range(0, 11):
        print(f"{numero} x {i} = {numero * i}")

numero = int(input("Ingrese el número del cual quiera saber la tabla de multiplicar: "))

tabla_multiplicar(numero)
# 7. Crear una función llamada operaciones_basicas(a, b) que reciba
# dos números como parámetros y devuelva una tupla con el resulta
# do de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los re
# sultados de forma clara.
def operaciones_basicas(a, b):
    suma =  a + b
    resta = a - b
    multiplicar = a * b
    dividir = a / b

    resultados_operaciones = (suma, resta, multiplicar, dividir)
    print(f"Resultado de las operaciones: ")
    print(f"\nSuma: {resultados_operaciones[0]}")
    print(f"\nResta: {resultados_operaciones[1]}")
    print(f"\nMultiplicación: {resultados_operaciones[2]}")
    print(f"\nDivisión: {resultados_operaciones[3]}")

a = float(input("Ingrese el primer elemento: "))
b = float(input("Ingrese el segundo elemento: "))

operaciones_basicas(a, b)
# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el
# peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC). Solicitar al usuario los datos y llamar a la fun
# ción para mostrar el resultado con dos decimales.
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)

    print(f"Su IMC es: {imc}")

peso = float(input("Ingrese su peso: "))
altura = float(input("Ingrese su altura: "))

calcular_imc(peso, altura)
# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
# una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
# resultado usando la función.
def celsius_a_fahrenheit(celsius):
    return celsius * 1.8 + 32

celsius = float(input("Ingrese los datos celsius que quiera transformar: "))

fahrenheit = celsius_a_fahrenheit(celsius)

print(f"El equivalente de {celsius} grados celsius en grados faherenheit es: {fahrenheit}")
# 10.Crear una función llamada calcular_promedio(a, b, c) que reciba
# tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta
# función.
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

a = float(input("Ingrese el primer valor del promedio a calcular: "))
b = float(input("Ingrese el segundo valor del promedio a calcular: "))
c = float(input("Ingrese el tercer valor del promedio a calcular: "))

promedio = calcular_promedio(a, b, c)

print(f"El promedio de los 3 números ingresados es: {promedio}")