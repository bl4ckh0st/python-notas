#!/usr/bin/env python3

juegos = ["Super Mario Bros", "Zelda: Breath of the wild", "Cyberpunk 2077", "Final Fantasy VII"]
tope = 500
# Generos
generos = {
        "Super Mario Bros": "Aventura",
        "Zelda: Breath of the wild": "Aventura",
        "Cyberpunk 2077": "Rol",
        "Final Fantasy VII": "Rol"
        }
# Ventas y Stock
ventas_y_stock = {
        "Super Mario Bros": (400, 200),
        "Zelda: Breath of the wild": (600, 20),
        "Cyberpunk 2077": (60, 120),
        "Final Fantasy VII": (924, 3)
}
# Clientes
clientes = {
        "Super Mario Bros": {"Celeste", "Vanessa", "Perla", "Alejandra", "Alondra"},
        "Zelda: Breath of the wild": {"Elizabeth", "Maria", "Vanessa", "Celeste", "Jessi"},
        "Cyberpunk 2077": {"Celeste", "Maria", "Raquel", "Adriana", "Elizabet"},
        "Final Fantasy VII": {"Vanessa", "Alondra", "Jessi", "Perla", "Cnthia"}
}
#mi_juego = "Super Mario Bros"

def sumario(juego):
#sumario
    print(f"\n[i] Resumen del juego {juego}\n")
    print(f"\t[+] Genero del juego: {generos[juego]}")
    print(f"\t[+] Total de ventas para este juego {ventas_y_stock[juego][0]} unidades")
    print(f"\t[+] Total de stock para este juego {ventas_y_stock[juego][1]} unidades")
    print(f"\t[+] Clientes para este juego: {', '.join(clientes[juego])}")

for juego in juegos: # no crean conflictos porque la funcion es privada o local
    if ventas_y_stock[juego][0] > 500: # primer elemento indice 0 es 1
        sumario(juego)

ventas_totales = lambda: sum(ventas for ventas, _ in ventas_y_stock.values()) # la barra baja indica que no interesa el segundo eemento pero hay que contemplarlo para acceder a otro daro
print(f"[+] El total de ventas de todos los productos ha sido de {ventas_totales()} productos") # calcula el numero de ventas de todos los productos

ventas_totales = lambda: sum(ventas for juego, (ventas, _) in ventas_y_stock.items() if ventas_y_stock[juego][0] > tope) # A diferencia de .values es items()  
print(f"[+] El total de ventas de todos los productos ha sido de {ventas_totales()} productos") # calcula el numero de ventas de todos los productos


