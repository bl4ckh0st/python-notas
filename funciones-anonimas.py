#!/usr/bin/python3
# funcion anonima lambda
print("\nFuncion anonima lamnda")
mi_funcion = lambda: "Hola Mundo"
print(mi_funcion())

# con argumentos
print("\nFuncion lambda anonima al cuadrado")
cuadrado = lambda x: x**2
print(cuadrado(8))

# una suma
print("\nFuncion lambda anonima con sumas")
suma = lambda x, y: x+y
print (suma(23, 5))

#con lista
numeros = [1, 2, 3, 4, 5]
cuadrados = map(lambda x: x**2, numeros)
for numero in cuadrados:
    print(numero)
# 
cuadrados = list(map(lambda x: x**2, numeros))
print(cuadrados)

# pares
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)

# 
from functools import reduce
producto = reduce(lambda x, y: x*y, numeros)
print(producto)


