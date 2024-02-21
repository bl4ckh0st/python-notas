#!/usr/bin/env python3

# Ejercicio sobre self y Objetos

# Hacer un programa que pida al usuario el nombre y la edad
# y trabajar con Objetos y todo lo que se ha visto en python3

nombre = input("Introduzca el nombre porfavor: ")
edad_str = input ("Introduzca la edad: ")
edad = int(edad_str)

class Persona(): #
    def __init__(self, nombre, edad): #  Persona.__init__(persona.nombre persona.edad)
        self.nombre = nombre # persona.nombre
        self.edad = edad  #  persona.edad

    def saludo(self):
        print (f"Su nombre es {self.nombre} y tiene {self.edad} primaveras")
persona = Persona(nombre, edad)
persona.saludo() # llamamos a una instancia llamada Persona

#-----Metodos de clase----
num_str = input("Introduzca un numero para saber si es un numero par o impar")
num = int(num_str)

class Calculadora:
    #  @@staticmethod
    def division(num):
       
        if num % 2 == 0:
            print (f"El numero {num} es par")
        else:
            print (f"El numero {num} es impar")
Calculadora.division(num)






