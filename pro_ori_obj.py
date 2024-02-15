#!/usr/bin/env python3

# Clases
# Metodos son funciones internas propias de la clase

class Persona:
    
    def __init__(self, nombre, edad): # Persona.__init__(celeste, nombre, edad)
    
        self.nombre = nombre
        self.edad = edad

    def saludo(self): #Persona.saludo(celeste)
        return f"Hola, se trata de {self.nombre} y tiene {self.edad} anos"

celeste = Persona("Celeste", 25) # celeste se convierte en objeto al estar instanciando esta clase
america = Persona("America", 23)
print(celeste.saludo())
print(america.saludo()) 

class Animal:
    def __init__(self, nombre, animal): # se pone self porque se declaran objetos
        self.nombre = nombre     # Animal.__init__(gato, nombre, animal)
        self.animal = animal
    def descripcion(self):# Animal.descripcion(objeto)
        print (f"{self.nombre} es un {self.animal}")

gato = Animal("Mocho", "Gato")
perro = Animal("Lobo", "Perro")
gato.descripcion()
perro.descripcion()
#-------------------------
class CuentaBancaria:
    def __init__(self, cuenta, nombre, dinero=0): # self.dinero es el dinero del objeto
        self.cuenta = cuenta        # dinero a secas es el propio argumento del metodo de l clase
        self.nombre = nombre
        self.dinero = dinero   # def es un metodo 
    def depostiar_dinero(self, dinero): # CuentaBancaria.depostiar_dinero(loerna)
        self.dinero += dinero
        print(f"\nSe han depositado a {self.nombre} {dinero} euros, actualmente el balance de la cuenta es de {self.dinero} euros")
    def retirar_dinero(self, dinero):
        if dinero > self.dinero:
            return f"\nOperacion denegada, fondos insuficientes {self.nombre}\n"
        self.dinero -= dinero

        return f"\nSe han retirado de {self.nombre} {dinero} euros, actualmente el balance de la cuenta es de {self.dinero} euros"

lorena = CuentaBancaria("1847623", "Lorena Patroski", 1000)
elizabeth = CuentaBancaria("8939293", "Elizabeth Vel", 10)
print(lorena.depostiar_dinero(500))
print(lorena.retirar_dinero(900))
print (elizabeth.retirar_dinero(20))
# -----------------

class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
    def area(self): # Rectangulo.area(rect1)
        return self.ancho * self.alto

    def __str__(self): # sirve para indicar que quiero que me muestre un objeto 
                       # porque si no se declara este metodo entonces el objeto 
                       # imprimira solo la direccion de memoria del objeto
       return f"\nPropiedades del rectangulo [Ancho: {self.ancho}][Alto: {self.alto}]"
    
    def __eq__(self, rect2): # este es un metodo de igualdad es un metodo especial
       return self.ancho == rect2.ancho and self.alto == rect2.alto # no causa conflicto porqe la variable dentro del metodo rect2 y la que esta afuera son distintas la del metodo es interna y la otra es externa
        


rect1 = Rectangulo(20, 80)
rect2 = Rectangulo(10, 60)

print(f"\nEl area es {rect1.area()}")
print(f"\nSon iguales? -> {rect1 == rect2}")
