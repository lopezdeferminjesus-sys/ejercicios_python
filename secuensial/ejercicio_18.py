<<<<<<< HEAD
# Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales.

nombre = input("Dime tu nombre: ")
apellido1 = input("Dime tu primer apellido: ")
apellido2 = input("Dime tu segundo apellido: ")

# Obtener iniciales
inicial = nombre[0]
inicial += apellido1[0]
inicial += apellido2[0]

# Convertir a mayúsculas
inicial = inicial.upper()

# Mostrar resultado
print("Las iniciales son:", inicial)
=======
<<<<<<<< HEAD:condicionales/ejercicio_8.py
"""
//Algoritmo que pida dos números 'nota' y 'edad' y un carácter 'sexo' 
//y muestre el mensaje 'ACEPTADA' si la nota es mayor o igual a cinco, 
//la edad es mayor o igual a dieciocho y el sexo es 'F'. 
//En caso de que se cumpla lo mismo, pero el sexo sea 'M', debe imprimir 'POSIBLE'. 
//Si no se cumplen dichas condiciones se debe mostrar 'NO ACEPTADA'.
"""

nota = int(input("Introduce la nota: "))
edad = int(input("Introduce la edad: "))
sexo = input("Introduce el sexo (F/M): ")

if nota >= 5 and edad >= 18:
    if sexo.upper() == "F":
        print("ACEPTADA")
    else:
        if sexo.upper() == "M":
            print("POSIBLE")
        else:
            print("NO ACEPTADA")
else:
    print("NO ACEPTADA")
========
# Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales.

nombre = input("Dime tu nombre: ")
apellido1 = input("Dime tu primer apellido: ")
apellido2 = input("Dime tu segundo apellido: ")

# Obtener iniciales
inicial = nombre[0]
inicial += apellido1[0]
inicial += apellido2[0]

# Convertir a mayúsculas
inicial = inicial.upper()

# Mostrar resultado
print("Las iniciales son:", inicial)
>>>>>>>> 7966bb8106b6481c8378fff94457e3e8c0d27ef4:secuensial/ejercicio_18.py
>>>>>>> 7966bb8106b6481c8378fff94457e3e8c0d27ef4
