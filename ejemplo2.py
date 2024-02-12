#!/usr/bin/python3

ip_address = "192.168.100.172"

print(ip_address)
print(type(ip_address))


my_ports = []
my_ports.append(22)
my_ports.append(80)
my_ports.append(443)

print(my_ports[0])
print(my_ports[1])
print(my_ports[2])

del my_ports[0] # elimina de la lista el elemento de la posicion 0

# aqui imprime por medio de bucle for
for port in my_ports:
        print("puerto " + str(port))
        print (f"puerto: {port}")

print(f"\n[+] La lista tiene un total de {len(my_ports)} elementos")

my_ports_2 = [10, 20, 30, 40, 50]
my_ports_2 += [22, 443, 80] # = my_ports_2 = my_ports_2 + [22, 443, 80]
my_ports_2  = sorted(my_ports_2) # Ordena la lista
print(f"\n[+] La lista tiene un total de {len(my_ports_2)} elementos")

my_ports_2[:4] # muestra los primeros 4 elementos
my_ports_2[4] # Muestra el 4 elemento
my_ports_2[2:4] # Muestra los elementos a partir de la posicion 2 al 4 tomando en cuenta el 0 como 1
my_ports_2[3:] # se muestra del 3 en delante
my_ports_2[-1] # muestra a partir del final
my_ports_2[-2:] # del final se cuenta dos para atras en adelante
my_ports_2[:-2] # se cuenta la posicion en el final hacia atras

my_ports_2.insert(2,32) # inserta el numero 32 en la posicion 2 contando desde el 0 como 1
my_ports_2.pop() # elimina la ultima posicion de una lista
my_ports_2.index(30) # muestra en la lista cuya posicion de elemento 30 en este caso es el 2
my_ports_2.count(22) # Muestra cuantas veces se repite el numero 22 de una lista

indices = [for x, y in enumerate(my_ports_2) if y==30 ] # muestra una lista cuyos indices valen 30


