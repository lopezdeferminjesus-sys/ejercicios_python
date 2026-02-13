<<<<<<< HEAD
# Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos. 
# El tiempo de viaje hasta llegar a otra ciudad B es de T segundos. 
# Escribir un algoritmo que determine la hora de llegada a la ciudad B.



horapartida = int(input("Hora de salida: "))
minpartida = int(input("Minutos de salida: "))
segpartida = int(input("Segundos de salida: "))

segviaje = int(input("Tiempo que has tardado en segundos: "))

seginicial = horapartida * 3600 + minpartida * 60 + segpartida

segfinal = seginicial + segviaje

horallegada = segfinal // 3600
minllegada = (segfinal % 3600) // 60
segllegada = (segfinal % 3600) % 60

print("Hora de llegada")
print(f"{horallegada}:{minllegada}:{segllegada}")
=======
<<<<<<<< HEAD:condicionales/ejercicio_7.py
"""
// Realiza un algoritmo que calcule la potencia, para ello pide por teclado 
//la base y el exponente. Pueden ocurrir tres cosas:
// * El exponente sea positivo, sólo tienes que imprimir la potencia.
// * El exponente sea 0, el resultado es 1.
// * El exponente sea negativo, el resultado es 1/potencia con el exponente positivo.
"""


base = int(input("Dime la base: "))
exponente = int(input("Dime el exponente: "))

if exponente > 0:
    print("La potencia es", base ** exponente)
else:
    if exponente == 0:
        print("La potencia es 1")
    else:
        print("La potencia es", 1 / (base ** abs(exponente)))
========
# Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos. 
# El tiempo de viaje hasta llegar a otra ciudad B es de T segundos. 
# Escribir un algoritmo que determine la hora de llegada a la ciudad B.



horapartida = int(input("Hora de salida: "))
minpartida = int(input("Minutos de salida: "))
segpartida = int(input("Segundos de salida: "))

segviaje = int(input("Tiempo que has tardado en segundos: "))

seginicial = horapartida * 3600 + minpartida * 60 + segpartida

segfinal = seginicial + segviaje

horallegada = segfinal // 3600
minllegada = (segfinal % 3600) // 60
segllegada = (segfinal % 3600) % 60

print("Hora de llegada")
print(f"{horallegada}:{minllegada}:{segllegada}")
>>>>>>>> 7966bb8106b6481c8378fff94457e3e8c0d27ef4:secuensial/ejercicio_17.py
>>>>>>> 7966bb8106b6481c8378fff94457e3e8c0d27ef4
