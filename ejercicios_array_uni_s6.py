# Ejercicio 1:
# 1.	Crea un arreglo unidimensional con nombre arregloA y de tamaño 100, con elementos aleatorios de números enteros del 0 al 500.
# 2.	Muestra por pantalla solo los valores que se encuentren en los índices pares del arreglo.
# 3.	Muestra el elemento mayor del arreglo.
# 4.	Muestra el índice (posición) del elemento mayor.
# 5.	Muestra el elemento menor del arreglo.
# 6.	Genera la copia de arreglo A y multiplicar por 3 cada elemento. Mostrar resultado.
# 7.	Muestra la suma de los elementos del segundo arreglo.
# 8.	Calcula el promedio de los elementos del segundo arreglo.

import random

print("Ejercicio 1: ")
# Crear arreglo unidimensional
arregloA = [random.randint(0,500) for _ in range(100)]
print(arregloA)

# Mostrar solo valores de indices pares
print(f"Valores de elemnentos en indices pares: {arregloA[::2]}")

# Mostrar elemento mayor
elemento_mayor = max(arregloA)
print(f"El elemento mayor es: {elemento_mayor}")

# Mostrar indice del elemento mayor
indice_mayor = arregloA.index(elemento_mayor)
print(f"El indice del elemento mayor es: {indice_mayor}")

# Mostrar elemento menor
elemento_menor = min(arregloA)
print(f"El elemento menor es: {elemento_menor}")

# Crear copia y multiplicar por 3 cada elemento
arregloA_x3 = arregloA[:].copy()
arregloA_x3 = [num * 3 for num in arregloA_x3]
print(f"Los elementos multiplicados por 3 son: {arregloA_x3}")

# Mostrar suma segundo arreglo
suma_arreglo2 = sum(arregloA_x3)
print(f"La suma de los elementos del segundo arreglo es: {suma_arreglo2}")

# Promedio elementos segundo arreglo
prom_arreglo2 = (suma_arreglo2/len(arregloA_x3))
print(f"El promedio de los elementos es: {prom_arreglo2}")


# Ejercicio 2:
# 1.	Crea un arreglo unidimensional con nombre arreglo_1 y de tamaño 10, con elementos aleatorios de números enteros del 0 al 1000.
# 2.	Muestra por pantalla todos los elementos del arreglo.
# 3.	Cuenta los elementos pares.
# 4.	Suma los elementos impares.
# 5.	Emite mensaje de cada elemento que sea primo.

import random

print("Ejercicio 2: ")

# Crear arreglo
arreglo_1 = [random.randint(0,1000) for _ in range (10)]

# Mostrar elementos del arreglo
print(f"Los elementos del arreglo son: {arreglo_1}")

# Contar elementos pares
contador_pares = 0

for num in arreglo_1:
    if num % 2 == 0:
        contador_pares += 1

print(f"La cantidad de elementos pares es: {contador_pares}")

# sumar elementos impares
suma_impares = 0

for imp in arreglo_1:
    if imp % 2 != 0:
        suma_impares += imp

print(f"La suma de los elementos impares es: {suma_impares}")

# Mostrar elementos primos
primos = []
def es_primo(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for n in range(3, num):
        if num % n == 0:
            return False
    return True

for i in arreglo_1:
    if es_primo(i):
        primos.append(i)


print(f"Los numeros primos son: {primos}")


# Ejercicio 3:
# 1.	Crear dos arreglos unidimensionales con nombre A y B y de tamaño 10, con elementos aleatorios de números enteros del 0 al 300.
# 2.	Muestra por pantalla la suma de los elementos de cada arreglo.
# 3.	Muestra por pantalla la suma de los elementos de ambos arreglos.
# 4.	Muestra por pantalla la tabla de multiplicar de los elementos impares del arreglo B.

import random

print("Ejercicio 3: ")

A = [random.randint(0,300) for _ in range (10)]
B = [random.randint(0,300) for _ in range (10)]

# Suma de cada arreglo

sumaA = sum(A)
sumaB = sum(B)

print(f"La suma de los elementos del arreglo A es: {sumaA}")
print(f"La suma de los elementos del arreglo B es: {sumaB}")

# Suma de ambos arreglos

sumaAB = sumaA + sumaB

print(f"La suma de ambos arreglos es: {sumaAB}")

# Tabla multiplicar elementos impares arreglo B

for n in B:
    if n % 2 != 0:
        print(f"Tabla de multiplicar del número {n}: ")
        for i in range(1,11):
            print(f"{n} x {i} = {n*i}")
        print()