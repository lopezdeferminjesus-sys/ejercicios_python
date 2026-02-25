precio_inicial = float(input("Introduce el precio inicial por kilo de la UVA (centimos): "))
kilos = int(input("Introduce cuantos kilos has vendido: "))
tipo = input("Introduce el tipo de la UVA (A/B): ")

if tipo.upper() != "A" and tipo.upper() != "B":
    print("Tipo incorrecto")
else:
    tamano = input("Introduce el tamaño de la UVA (1/2): ")
    
    if tamano != "1" and tamano != "2":
        print("Tamaño incorrecto")
    else:
        if tipo.upper() == "A":
            if tamano == "1":
                precio_inicial = precio_inicial + 20
            else:
                precio_inicial = precio_inicial + 30
        else:
            if tamano == "1":
                precio_inicial = precio_inicial - 20
            else:
                precio_inicial = precio_inicial - 30
        
        precio_final = precio_inicial * kilos
        print("La ganancia es", precio_final / 100, "euros.")