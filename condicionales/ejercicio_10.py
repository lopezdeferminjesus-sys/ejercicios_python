"""
//Algoritmo que pida los puntos centrales x1,y1,x2,y2 y los radios r1,r2 de dos 
//circunferencias y las clasifique en uno de estos estados:
//exteriores
//tangentes exteriores
//secantes
//tangentes interiores
//interiores
//concéntricas
"""

x1 = float(input("x1: "))
y1 = float(input("y1: "))
r1 = float(input("r1: "))

x2 = float(input("x2: "))
y2 = float(input("y2: "))
r2 = float(input("r2: "))

distancia = ((x2 - x1) * 2 + (y2 - y1) * 2) ** 0.5

if distancia == 0:
    print("Concéntricas")
elif distancia > r1 + r2:
    print("Exteriores")
elif distancia == r1 + r2:
    print("Tangentes exteriores")
elif distancia > abs(r1 - r2):
    print("Secantes")
elif distancia == abs(r1 - r2):
    print("Tangentes interiores")
else:
    print("Interiores")