#!/usr/sbin/python3
# vulenrabilidades
cve_list = ['CVE-2023-1435', 'CVE-2022-45761', 'CVE-2023-7863'] # vulnerabilidades
cve_list.remove('CVE-2023-7863') #remueve elemento indicado

puertos_tcp = [21, 22, 25, 80, 443, 445, 8080, 9099, 69]
puertos_tcp.append(1337)
puertos_tcp.sort()
print(puertos_tcp)

for puerto in puertos_tcp:
    print(f"\nEste es el puerto {puerto}")

attacks = ['Phishing','DDoS','SQL Injection', 'Man In The Middle', 'Cross-site scripting']
primer_ataque = attacks[2] # aqui imprime SQL Injection porque siempre cuenta el 0
print(primer_ataque)
otro_ataque = attacks[:3] # imprime los tres primeros Phishing, DDoS, SQL Injectio
print(otro_ataque) # los dos puntos representa el lado donde contaran 
otro_ataque_mas = attacks[3:] # imprime los dos ultimos, MITM y XSS porque cuenta apartir de 3 posicion contando el 0
print(otro_ataque)
ataque_extra = attacks[2:4] # cuenta desde SQL Injection hasta MITM, 
print(ataque_extra)         # el 4 ya no se cuenta, es el limitante

i = 0 # contador

while i < len(attacks): #len utiliza para contar el numero de elementos de una lista   
    print(attacks[i])
    i += 1 
    if i >= len(attacks): # este sirve para hacer una comparacion si el contador tiene mas elementos
        print("\nse ha concluido el while")
# otra forma de recorrer listas:
for i, attack in enumerate(attacks):
    print(f"Para la posicion {i} tendriamos el ataque {attack}")

attacks_uppercase = [attack.upper() for attack in attacks]
print(attacks_uppercase) #upper espara poner en mayusculas y lower para minuscula

#----------------------------
names = ["S4vitar", "Hackermate", "Lobotec", "Hackavis"]
edades = [27, 45, 13, 20]
for name, edad in zip(names, edades):
    print(f"{name} tiene {edad} anos")
   # names.clear() # limpia toda la lista
names[2] = "Chema Alonso" # Reemplaza a Lobotec por Chema Alonso
elemento_borrado = names.pop(1) # pop elimina un elemento de una lista
print(f"\nEl elemento eliminado es {elemento_borrado}")
mas_names = ["bl4ckh0st", "Celesteee"]
names.extend(mas_names)
print(names)
