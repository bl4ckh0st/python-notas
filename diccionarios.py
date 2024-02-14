#!/usr/sbin/env python3

mi_diccionario = {"nombre": "Celeste", "edad": 25, "estado": "Chihuahua", "profesion": "Sistemas" }

print(mi_diccionario["estado"])
print(mi_diccionario["edad"])
print(mi_diccionario["nombre"])
print (mi_diccionario["profesion"])

del mi_diccionario["edad"] # elimina la clave edad 
if "nombre" in mi_diccionario:
    print("Esta clave existe en el diccionario")
else:
    print("Esta clave no existe en el diccionario")
# muestra la valve y el valor en una iteracion for
for key, value in mi_diccionario.items():
    print(f"Para la clave {key} tendriamos el valor {value}")
# con len() muestra la longitud de los elementos en el diccionario
print(f"La longitud del diccionario es de {len(mi_diccionario)} elementos")

cuadrados = {x: x**2 for x in range(6)} # se pone x: para representar que la x vale 0 y no null
print(cuadrados)
print(cuadrados.keys())
print(cuadrados.values())

# sirve para buscar, devuelve un booleano en este caso un false donde no encuentra la edad 
print(mi_diccionario.get("edad", "No encontrado"))
mi_diccionario_dos = {"mascotas": "perro", "color": "rosa"}
mi_diccionario.update(mi_diccionario_dos)
print(mi_diccionario["color"])

my_dict = {
        "nombre": "Celeste", "Estado": "Chihuahua",
        "hobbies": {"primero": "musica country", "segundo": "sonreir"},
        "edad": 25
        }
print(len(my_dict))
print(my_dict["hobbies"]["segundo"])

for elemento in my_dict:
    print(elemento)     # aqui imprimira el nombre de elemento ejemplo nombre
for elemento in my_dict.values(): #
    print (elemento)    # aqui imprime el valor del elemento

for key, value in my_dict.items():
    print(f"[{key}]: {value}")
# Para verificar una clave en un diccionario es con la palabra 'in'
