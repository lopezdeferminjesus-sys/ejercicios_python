<<<<<<< HEAD
# Dos vehículos viajan a diferentes velocidades (v1 y v2) y están distanciados 
# por una distancia d. 
# El que está detrás viaja a una velocidad mayor. Se pide hacer un algoritmo 
# para ingresar la distancia entre los dos vehículos (km) y sus respectivas 
# velocidades (km/h) y con esto determinar y mostrar en que tiempo (minutos) 
# alcanzará el vehículo más rápido al otro.

velocidad1 = float(input("Dime la velocidad del coche 1 (km/h): "))
velocidad2 = float(input("Dime la velocidad del coche 2 (más pequeña) (km/h): "))
distancia = float(input("Dime la distancia entre los coches (km): "))

tiempo = distancia / (velocidad1 - velocidad2)

tiempo = tiempo * 60

print("Lo alcanza en", tiempo, "minutos.")
=======
<<<<<<<< HEAD:condicionales/ejercicio_6.py
"""
Programa que lea una cadena por teclado y compruebe si es una letra mayúscula.
"""


cad = input("Introduce una cadena: ")

if cad == cad.upper():
    print("La cadena es mayúsculas")
else:
    print("La cadena no es mayúsculas")
========
# Dos vehículos viajan a diferentes velocidades (v1 y v2) y están distanciados 
# por una distancia d. 
# El que está detrás viaja a una velocidad mayor. Se pide hacer un algoritmo 
# para ingresar la distancia entre los dos vehículos (km) y sus respectivas 
# velocidades (km/h) y con esto determinar y mostrar en que tiempo (minutos) 
# alcanzará el vehículo más rápido al otro.

velocidad1 = float(input("Dime la velocidad del coche 1 (km/h): "))
velocidad2 = float(input("Dime la velocidad del coche 2 (más pequeña) (km/h): "))
distancia = float(input("Dime la distancia entre los coches (km): "))

tiempo = distancia / (velocidad1 - velocidad2)

tiempo = tiempo * 60

print("Lo alcanza en", tiempo, "minutos.")
>>>>>>>> 7966bb8106b6481c8378fff94457e3e8c0d27ef4:secuensial/ejercicio_16.py
>>>>>>> 7966bb8106b6481c8378fff94457e3e8c0d27ef4
