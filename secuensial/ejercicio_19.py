<<<<<<< HEAD
# Escribir un algoritmo para calcular la nota final de un estudiante, considerando que: 
# por cada respuesta correcta 5 puntos, por una incorrecta -1 y por respuestas en 
# blanco 0. Imprime el resultado obtenido por el estudiante.

correctas = int(input("Dime cantidad de respuestas correctas: "))
incorrectas = int(input("Dime cantidad de respuestas incorrectas: "))

puntos = correctas * 5 + incorrectas * (-1)

print("Puntos:", puntos)
=======
<<<<<<<< HEAD:condicionales/ejercicio_9.py
"""
Algoritmo que pida tres números y los muestre ordenados (de mayor a menor);
"""


num1 = int(input("Dime el número 1: "))
num2 = int(input("Dime el número 2: "))
num3 = int(input("Dime el número 3: "))

if num1 > num2 and num1 > num3:
    if num2 > num3:
        print(num1, num2, num3)
    else:
        print(num1, num3, num2)

if num2 > num1 and num2 > num3:
    if num1 > num3:
        print(num2, num1, num3)
    else:
        print(num2, num3, num1)

if num3 >= num1 and num3 >= num2:
    if num1 > num2:
        print(num3, num1, num2)
    else:
        print(num3, num2, num1)
========
# Escribir un algoritmo para calcular la nota final de un estudiante, considerando que: 
# por cada respuesta correcta 5 puntos, por una incorrecta -1 y por respuestas en 
# blanco 0. Imprime el resultado obtenido por el estudiante.

correctas = int(input("Dime cantidad de respuestas correctas: "))
incorrectas = int(input("Dime cantidad de respuestas incorrectas: "))

puntos = correctas * 5 + incorrectas * (-1)

print("Puntos:", puntos)
>>>>>>>> 7966bb8106b6481c8378fff94457e3e8c0d27ef4:secuensial/ejercicio_19.py
>>>>>>> 7966bb8106b6481c8378fff94457e3e8c0d27ef4
