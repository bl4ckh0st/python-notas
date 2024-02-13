#!/usr/bin/python3

def saludo():
    print("\nHola mundo!")

saludo()    # Una funcion es un bloque de codigo que estamos reutilizando y realiza una tarea especifica

def saludo(nombre):
    print(f"\nHola {nombre}")

saludo("Celeste")

# con una suma
def suma(x, y):
    return x + y
resultado = suma(2, 8)
print(f"\nLa suma de ambos valores es {resultado}")


# funciones y variables locales y globales
variable = "soy global"

def mi_funcion():
    global variable # global modifica una variable global dentro de una funcion
    variable = "soy local"
    print(variable)
mi_funcion()
print(variable)
