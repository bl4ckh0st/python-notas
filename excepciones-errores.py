#!/usr/bin/python3
try:
       num = 5/0
#except: 
except ZeroDivisionError:
    print("No se puede dividir un numero entre cero")
    
from pwn import log #para el log.failure log.success libreria para colores
try:
        num = "hola"/0
except TypeError:
    print("Solo es posible dividir solo numeros enteros")    
    log.failure("Las operatorias matematicas solo sin divisible entre numeros")
else:
    print(f"La division de ambos numeros da como resultado {num}")
finally:
    log.success("Esto siempre se va a ejecutar el finally")

# raise
x = -5
if x < 0:
    raise Exception("No se pueden utilizar numeros negativos")
# para ver el tipo de excepcion tan solo hay que ejecutar el error en consola
