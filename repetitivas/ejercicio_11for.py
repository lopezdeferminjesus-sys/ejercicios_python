numero = int(input("Introduce un número para comprobar si es primo: "))

es_primo = True

if numero <= 1:
    es_primo = False
else:
    for num in range(2, int(numero ** 0.5) + 1):
        if numero % num == 0:
            es_primo = False
            break

if es_primo:
    print("Es Primo")
else:
    print("No es Primo")