#!/usr/bin/env  python3
#
class Persona: # En este caso usaremos la variable objeto en vez de self 
    def __init__(objeto, nombre, edad):  # Persona.__init__(celeste, nombre, edad)
        objeto.nombre = nombre  # celeste.noombre = "Celeste"
        objeto.edad = edad #  # celeste.edad  =  25

    def presentacion(objeto):
         print(f"Hola {objeto.nombre} es hermosa y tiene {objeto.edad} primaveras") # celeste.nombre celeste.edad
celeste = Persona("Celeste", 25)
celeste.presentacion()

#---------------------------------------------
# Calculadora
#
class Calculadora:
    def __init__(self, num): # Calculadora.__init__(calc, num)
        self.num = num # calc.num = 5

    def suma(self, otro_num): # Calculadora.suma(calc, 8)
        return self.num + otro_num # calc.num + 8 -> 5 + 8 

    def doble_suma(self, num1, num2): # Calculadora.doble_suma(calc, 2, 9)
        return self.suma(num1) + self.suma(num2)




calc = Calculadora(5)
calc.suma(8)
print(calc.doble_suma(2, 9))
