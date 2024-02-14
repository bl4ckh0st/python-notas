#!/usr/sbin/env python3

mi_conjunto = {1, 2, 3}
mi_conjunto.add(4) # se agrega el numero numero 4 al conjunto no tiene un orden
mi_conjunto.update({4, 5, 6}) # inserta estos 3 elementos a mi_conjunto
mi_conjunto.remove(3) # se elimina el elemento 3 aqui el cero no es inicial
mi_conjunto.discard(9) # a diferencia de remove, discard no sale error al no encontrar un elemento inexistente
print(mi_conjunto)
# NOTA: En los conjuntos no existen elementos repetidos ejemplo en el add y el update en el ejemplo anterior.

segundo_conjunto = {2, 3, 4, 6}
conjunto_intersection = mi_conjunto.intersection(segundo_conjunto)
print(conjunto_intersection) # muestra los elementos repetidos entre los dos conjuntos
conjunto_union = mi_conjunto.union(segundo_conjunto) 

print(mi_conjunto.issubset(segundo_conjunto)) # un booleano para ver si es subconjunto el uno con el dos

mi_lista = [1, 1 ,1, 3, 4, 3, 4, 7, 6, 5, 4, 6, 8, 9, 5]
no_repeat = list(set(mi_lista))
print(no_repeat)    # esto hace que no se repitan numeros en una lista y se puede convertir en un conjunto

print("Diferencias entre conjuntos") # muestra la diferencia entre los elementos de los conjuntos .difference
diferenias_entre_conjuntos = mi_conjunto.difference(segundo_conjunto)
print(diferenias_entre_conjuntos)

mi_conjunto = range(1000)
print(1234 in mi_conjunto) # pregunta a conjunto si existe el 1234


