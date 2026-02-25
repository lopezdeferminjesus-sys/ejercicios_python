cant_a_mostrar = 0

while cant_a_mostrar <= 0:
    cant_a_mostrar = int(input("Ingrese la cantidad de números primos a mostrar: "))

print("1: 2")

cant_mostrados = 1
num = 3 

while cant_mostrados < cant_a_mostrar:

    es_primo = True  

    divisor = 3
    while divisor * divisor <= num and es_primo == True:

        if num % divisor == 0:
            es_primo = False

        divisor += 2  

    if es_primo == True:
        cant_mostrados += 1
        print(str(cant_mostrados) + ": " + str(num))

    num += 2  