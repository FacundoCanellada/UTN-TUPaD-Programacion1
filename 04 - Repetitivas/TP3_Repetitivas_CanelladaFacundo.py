import random
#Actividades
# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea. 
num = 0

for i in range(0,101):
    print(num)
    num += 1

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de 
# dígitos que contiene. 
numEntero = int(input("Ingrese un numero entero por favor: "))
digito = 0
while numEntero > 0:
    numEntero //= 10
    digito += 1
print(f"La cantidad de digitos que contiene el numero es: {digito}")

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores 
# dados por el usuario, excluyendo esos dos valores. 

num1 = int(input("Ingrese el primer numero por favor: "))
num2 = int(input("Ingrese el segundo numero por favor: "))
suma = 0
for i in range(num1 + 1, num2):
    suma += i
print(f"La suma de los numeros enteros comprendidos entre {num1} y {num2} es: {suma}")

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en 
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese 
# un 0. 
sumaSecuencia = 0
while True:
    numSecuencia = int(input("Ingrese un numero entero por favor (ingrese 0 para finalizar): "))
    if numSecuencia == 0:
        break
    sumaSecuencia += numSecuencia
print(f"La suma total de los numeros ingresados es: {sumaSecuencia}")

#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número. 
numeroAleatorio = random.randint(0,9)
cantidadIntentos = 0

while True:
    numeroUsuario = int(input("Ingrese un numero del 0 al 9 por favor: "))
    cantidadIntentos += 1
    if numeroUsuario == numeroAleatorio:
        print(f"¡Felicidades! Has adivinado el número en {cantidadIntentos} intentos.")
        break
    else:
        print("Número incorrecto. Inténtalo de nuevo.")


#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos 
# entre 0 y 100, en orden decreciente. 
for i in range(101, -1, -1):
    if i % 2 == 0:
        print(i)
    else:
        continue

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un 
# número entero positivo indicado por el usuario. 
numDefinido = 0
sum = 0

numUsuario = int(input("Ingrese un numero entero por favor: "))
while True:
    if numUsuario < 0:
        print("Por favor ingrese un numero entero positivo")
        numUsuario = int(input("Ingrese un numero entero por favor: "))
    else:
        break
for i in range(numDefinido, numUsuario + 1):
    sum += i
print(f"La suma de los numeros enteros comprendidos entre {numDefinido} y {numUsuario} es: {sum}")

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el 
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son 
# negativos y cuántos son positivos.
cantidadPermitida = 100 #modifcando este valor solamente, el programa puede procesar los numeros que sean necesarios
contadorPermitido = 0
contadorPares = 0
contadorImpares = 0
contadorNegativos = 0
contadorPositivos = 0

while True:
    numUsuario = int(input("Ingrese un numero entero por favor: "))
    contadorPermitido += 1

    if numUsuario % 2 == 0:
        contadorPares += 1
    else:
        contadorImpares += 1
    if numUsuario < 0:
        contadorNegativos += 1
    elif numUsuario > 0:
        contadorPositivos += 1
    if contadorPermitido == cantidadPermitida:
        print("Ha alcanzado el limite de intentos permitidos")
        break

print(f"Cantidad de numeros pares ingresados: {contadorPares}")
print(f"Cantidad de numeros impares ingresados: {contadorImpares}")
print(f"Cantidad de numeros negativos ingresados: {contadorNegativos}")
print(f"Cantidad de numeros positivos ingresados: {contadorPositivos}")


# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
# media de esos valores.
cantPermitida = 100 #modificando este valor solamente, el programa puede procesar los numeros que sean necesarios   
conPermitido = 0
contMedia = 0
sumatoria = 0

while True:
    numIngresado = int(input("Ingrese un numero entero por favor: "))
    conPermitido += 1
    contMedia += 1
    sumatoria += numIngresado
    if conPermitido == cantPermitida:
        print("Ha alcanzado el limite de intentos permitidos")
        break
print(f"El promedio de los numeros ingresados es: {sumatoria / contMedia}")

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el 
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745. 
numInvertir = int(input("Ingrese un numero entero por favor: "))
numInvertido = 0

while numInvertir > 0:
    digito = numInvertir % 10
    numInvertido = numInvertido * 10 + digito
    numInvertir //= 10
print(f"El numero invertido es: {numInvertido}")