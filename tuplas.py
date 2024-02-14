#!/usr/sbin/env python3

# las tuplas y las listas son semejantes pero son otro tipo de estructura de datos\
# a diferencia de las listas las tuplas son inmnutables, osea que no se puede modificar y se represente por () en vez de [] como las listas y {} los diccionarios
# (tuplas) [listas] {diccionarios}

ejemplo = (1, 2, 3, 4, 5)
print(ejemplo[0]) # muestra el primer elemento
print(ejemplo[1:3]) # muestra los elementos 2 y 3

#ejemplo[0] = 8 # sale un error porque las tuplas son inmnutables

for elemento in ejemplo:
    print(elemento)

a, b, c, d, e = ejemplo
print(a)
print(b)
print(c) 
print(d)
print(e)

ejemplo_dos = (6, 7, 8, 9)
suma_ejemplos = ejemplo + ejemplo_dos
print(suma_ejemplos)  #suma las dos tuplas y lo representa en tupla

numeros_pares = tuple(i for i in suma_ejemplos if i % 2 == 0)
print("\nNumeros pares")
print(numeros_pares)






