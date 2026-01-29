# Pide al usuario dos números y muestra la "distancia" entre ellos 
# (el valor absoluto de su diferencia, de modo que el resultado sea siempre positivo).

numero_1 = int(input("Dame el número 1: "))
numero_2 = int(input("Dame el número 2: "))

distancia = abs(numero_1 - numero_2)

print("La distancia absoluta es:", distancia)