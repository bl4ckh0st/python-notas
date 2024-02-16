#!/usr/bin/env python3

class Calculadora:

    @staticmethod
    def suma(num1, num2):

        return num1 + num2 

    @staticmethod
    def resta(num1, num2):
        
        return num1 - num2


    @staticmethod
    def multiplicacion(num1, num2):

        return num1 * num2

    @staticmethod
    def division(num1, num2):
    
        return num1 / num2 if num2 != 0 else "\n Error: No se puede dividir un numero entre cero"

print(Calculadora.suma(2, 8))
print(Calculadora.suma(8, 4))
print(Calculadora.multiplicacion(5, 10))
print(Calculadora.division(10, 0))

# --------------------------------------
#
# Metodos de Clase

class Automovil:
    def __init__(self, marca, modelo):

        self.marca = marca
        self. modelo = modelo

    @classmethod 
    def deportivos(cls, marca):
    
        return cls(marca, "Deportivo")

    def sean(cls, marca):
        
        return cls(marca, "Sean")

    def __str__(self):

        return f"\nLa marca {self.marca} es un modelo {self.modelo}"


deportivo = print(Automovil.deportivos("Ferrari")) 
sean = print(Automovil.deportivos("Toyota")) 

# --------------------------------

class Estudiantes ():

    estudiantes = []

    def __init__(self, nombre, edad):

        self.nombre = nombre
        self.edad = edad

        Estudiantes.estudiantes.append(self)

        
    @staticmethod # a diferencia de @classmethod, aqui no es necesario pasarle el self pporque no jugamos con objetos``
    def es_mayor_de_edad(edad):
        return edad >= 18
    
    @classmethod
    def crear_estudiante(cls, nombre, edad):
        if cls.es_mayor_de_edad(edad):
            return cls(nombre, edad)
        
        else:
            print(f"\nError el estudiante {nombre} es menor de edad")
    @staticmethod
    def mostrar_estudiantes():
        for i, estudiante in enumerate(Estudiantes.estudiantes):
            print(f"\tEstudiante numero [{i+1}]: {estudiante.nombre}")
        

Estudiantes.crear_estudiante("Celeste", 25)
Estudiantes.crear_estudiante("Karen", 29)
Estudiantes.crear_estudiante("Sandy", 15)
Estudiantes.crear_estudiante("America", 17)
print("\nMostrando los estudiantes existentes:\n")
Estudiantes.mostrar_estudiantes()
