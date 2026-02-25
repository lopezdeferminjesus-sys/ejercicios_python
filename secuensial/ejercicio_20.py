<<<<<<< HEAD
# Diseñar un algoritmo que nos diga el dinero que tenemos (en euros y céntimos) 
# después de pedirnos cuantas monedas tenemos de 2e, 1e, 50 céntimos, 20 céntimos 
# o 10 céntimos).

euro2 = int(input("Monedas de 2 euros: "))
euro1 = int(input("Monedas de 1 euro: "))
cent50 = int(input("Monedas de 50 céntimos: "))
cent20 = int(input("Monedas de 20 céntimos: "))
cent10 = int(input("Monedas de 10 céntimos: "))


total_euros = euro2 * 2 + euro1


total_centimos = cent50 * 50 + cent20 * 20 + cent10 * 10

total_euros += total_centimos // 100
total_centimos = total_centimos % 100

print(total_euros, "euros y", total_centimos, "céntimos.")
=======
<<<<<<<< HEAD:condicionales/ejercicio_10.py
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
========
# Diseñar un algoritmo que nos diga el dinero que tenemos (en euros y céntimos) 
# después de pedirnos cuantas monedas tenemos de 2e, 1e, 50 céntimos, 20 céntimos 
# o 10 céntimos).

euro2 = int(input("Monedas de 2 euros: "))
euro1 = int(input("Monedas de 1 euro: "))
cent50 = int(input("Monedas de 50 céntimos: "))
cent20 = int(input("Monedas de 20 céntimos: "))
cent10 = int(input("Monedas de 10 céntimos: "))


total_euros = euro2 * 2 + euro1


total_centimos = cent50 * 50 + cent20 * 20 + cent10 * 10

total_euros += total_centimos // 100
total_centimos = total_centimos % 100

print(total_euros, "euros y", total_centimos, "céntimos.")
>>>>>>>> 7966bb8106b6481c8378fff94457e3e8c0d27ef4:secuensial/ejercicio_20.py
>>>>>>> 7966bb8106b6481c8378fff94457e3e8c0d27ef4
