base = int(input("Dime la base: "))
exponente = int(input("Dime el exponente: "))

if exponente > 0:
    print("La potencia es", base ** exponente)
else:
    if exponente == 0:
        print("La potencia es 1")
    else:
        print("La potencia es", 1 / (base ** abs(exponente)))