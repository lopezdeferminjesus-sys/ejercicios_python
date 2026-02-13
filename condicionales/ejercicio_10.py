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


x1 = float(input("Dime coordenada x primera circunferencia: "))
y1 = float(input("Dime coordenada y primera circunferencia: "))
r1 = float(input("Dime radio primera circunferencia: "))

x2 = float(input("Dime coordenada x segunda circunferencia: "))
y2 = float(input("Dime coordenada y segunda circunferencia: "))
r2 = float(input("Dime radio segunda circunferencia: "))

distancia = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5

# Circunferencias exteriores
if distancia > (r1 + r2):
    print("Circunferencias exteriores")

# Tangentes exteriores
if distancia == (r1 + r2):
    print("Circunferencias tangentes exteriores")

# Secantes
if distancia < (r1 + r2) and distancia > abs(r1 - r2):
    print("Circunferencias secantes")

# Tangentes interiores
if distancia == abs(r1 - r2):
    print("Circunferencias tangentes interiores")

# Interiores
if distancia > 0 and distancia < abs(r1 - r2):
    print("Circunferencias interiores")

# Concéntricas
if distancia == 0:
    print("Circunferencias concéntricas")