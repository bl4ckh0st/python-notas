#!/usr/bin/env python3

class Libro:
    
    IVA = 0.21 # Las constantes a diferencia de las variables van en MAYUSCULAS
    #bestseller_value = 5000

    def __init__(self, titulo, autor, precio, bestseller_value=5000):
        
        self.titulo = titulo
        self.autor = autor
        self.precio = precio
        self.bestseller_value = bestseller_value


    @staticmethod # Este es un Decorador, el decorador hace referencia y no es necesario self
    def es_bestseller(instancia, total_ventas): # Libro.es_bestseller(total_ventas)
        
        #return total_ventas > Libro.bestseller_value # sin instancia
        return total_ventas > instancia.bestseller_value # con instancia declarando la variable dentro del metodo __init__
    @staticmethod
    def precio_iva(precio):

        return precio + precio * Libro.IVA

    @classmethod # La idea de este docarador recide como argumento en el propio metodo la propia clase, hay que poner cls para referenciar a la clase 

    def precio_iva(cls, precio):
        return precio + precio * cls.IVA


class LibroDigital(Libro): # Ejemplo de Herencias
    
    IVA = 0.16


mi_libro_digital = Libro("Primeros acercamiento", "John Doe", 20.20)
mi_libro = Libro("Como conquistas a Celeste", "John Doe", 20.20)
print(Libro.es_bestseller(mi_libro, 2000))
# round sirve para que solo muestre dos deciminales ejemplo de sintaxis y redondea
print(f"\nEl precio del libro con IVA es de {round(Libro.precio_iva(mi_libro.precio),2)}")
print(f"\nEl precio del libro digital con IVA incluido es de {round(LibroDigital.precio_iva(mi_libro_digital.precio),2)}")



