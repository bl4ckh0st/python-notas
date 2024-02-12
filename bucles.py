#!/usr/bin/python3
# bucle con for donde imprime una lista con las siguientes palabras
names = ["Palabra1", "Palabra2", "Palabra3", "Palabra4"]
for name in names:
    print(f"La palabra para esta vuelta es {name}")


# muestra un bucle con una secuencia del 0 al 4 
print("\nEjemplo de bucle con for y range del 0 al 4")
for i in range(5):
    print(i)

# bucle con while 
print("\nEjemplo de bucle con while en rango del 0 al 4")
i = 0
while i < 5:
    print(i)
    i += 1

# enumera en un bucle los nombres proporcionados
print("\nEnumera en un bucle los nombres declarados")
nombres = ["Alex", "Luisa", "Adriana", "Celeste"]
for contador, nombre in enumerate(nombres):
    print(f"Nombre [{contador+1}]: {nombre}")

# diccionarios
print("se emplea un diccionario con bucle for con ejemplo de frutas")
frutas = {"manzana": 1, "platano": 5, "durazno": 3}
for fruta, cantidad in frutas.items():
    print(f"Hay {cantidad} {fruta}(s)")

# Bucles anidados
print("\nDesgloza listad de distintos elementos ")
mi_lista = [[1, 4, 5],[2, 6, 8], [9, 4, 1]]
for element in mi_lista:
    print(f"\nVamos a desglozar la lista {element}")
    for element_in_list in element:
        print(element_in_list)

# Lista de comprension
print("\nEn esta lista de comprension se saca la exponenical de la lista de la lista declarada")
odd_list = [1, 3, 5, 7, 9]
cuadrado = [i ** 2 for i in odd_list]
print(cuadrado)
#-------------------
# funcion del break
print("\nSe ejecuta un for y se rompe en el 5 por el break y el if")
for i in range(10):
    print(i)
    if i == 5:
        break
# funcion del continue
print("\nSe ejecuta el for pero se salta la linea 5 por el conitnue")
for i in range(10):    
    if i == 5:
        continue
    print(i)
# condicionales if else:
print("\nCondicionales if y else")
for i in range(10):
    if i == 5:
        print(f"Actualmente 'i' vale 5 [{i}]")
    else:
        print(f"Actualmente 'i' NO vale 5 [{i}]")
else: # este es el else del for:
    print("[+] Bucle concluido exitosamente")

# bucle while :
print("\nBucle con while y su else con break")
i = 0
while i < 13:
    if i == 10:
        print("Salimos antes de tiempo")
        break
    i += 1 
else:
    print("El bucle termino normalmente")

# bucles con if elif y else:
edad = 28
nacionalidad = "argentino"
print("\nEjemplo de if y else")
if edad >= 18 and nacionalidad == "mexicana":
    print("Puedes votar en las elecciones mexicanas")
else:
    print("NO eres mexicano cabron")
# condicional anidado 
print("\ncondicional anidado")
if edad >= 18:
    if nacionalidad == "argentino":
        print("puedes votar en las elecciones argentinas")


# if y else para listas
print("\nEjemplo de if y else en listas")
mi_lista = [1, 4, 5, 14, 17, 20, 69]
if 20 in mi_lista:
    print("Este numero esta en la lista")
else:
    print("El numero no esta en la lista")

# Numeros par 
print("\nSacar si es par o impar")
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for numero in numeros:
    if numero % 2 == 0:
        print(f"El numero {numero} es par")
    else:
        print(f"El numero {numero} es impar")

# booleano
print("\nCondicionales con booleano")
numeros = [2, 4, 6, 8, 10, 12, 14]
todos_son_pares =  True
for numero in numeros:
    if numero % 2 != 0:
        todos_son_pares = False
        break # sale del bucle al encontrar un elemento que sea impar

if todos_son_pares:
    print("Todos los elementos de la lista son pares")
else:
    print("Algun de los elementos de la lista es impar")

