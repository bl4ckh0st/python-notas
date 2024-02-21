#!/usr/bin/env python3

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    def hablar(self):
        raise NotImplementedError("Las subclases deben implementar este metodo")
class Gato(Animal):
    
    def hablar(self):
        return f"Miau!"

class Perro(Animal):
    def hablar(self):
        return f"Guau!"

gato = Gato("Negrito")
perro = Perro("Wisky")
#gato_dos = Animal("mimi") # Si habilito este saldra el NotImplementedError
# porque no esta declarada a la sub clase que mande a llamar a gato_dos y esta mandando a Animal la clase padre

#---Polimorfismo
def hacer_hablar(self):

    print(f"{self.nombre} dice {self.hablar()}")


hacer_hablar(gato)
hacer_hablar(perro)
#print(gato.gato_dos())

#------------------------------
class Automovil:
    def __init__(self, marca, modelo):

        self.marca = marca
        self.modelo = modelo

    def describir(self):
        
        return f"Vehiculo: {self.marca} {self.modelo}"

class Coche(Automovil):
        
    def describir(self):

         return f"Coche: {self.marca} {self.modelo}"

class Moto(Automovil):

    def describir(self):
        return f"Moto: {self.marca} {self.modelo}"

def describir_vehiculo(vehiculo): # Polimorfismo

    print(vehiculo.describir())


coche = Coche("Toyota", "Corolla")
moto = Automovil("Honda", "CBR")

describir_vehiculo(coche)
describir_vehiculo(moto)

#------
class Dispositivo:
    def __init__(self, modelo):
        self.modelo = modelo

    def escanear_vulnerabilidades(self)
        raise NotImplementedError("Este metodo debe de ser definido para el resto de subclases existentes")

class Ordenador(Dispositivo):
    
    def escanear_vulnerabilidades(self):
        return f"Analisis de vulnerabilidades concluido: Actualizacion de software necesaria, Multiples desactualizaciones de software detectadas"
class Router(Dispositivo):
    def escanear_vulnerabilidades(slef):
        return f"Analisis de vulnerabilidades concluido: Multiples puertos criticos detectados como abiertos, es recomendable cerrar estos puertos"

class TelefonoMovil(Dispositivo):
    def escanear_vulnerabilidades(self):
        return f"Analisis de vulnerabilidades concluido: Multiples aplicaciones detectadas con permisos excesivos"

pc = Ordenador("Dell XPS")

