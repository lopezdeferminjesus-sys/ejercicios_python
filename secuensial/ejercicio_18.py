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