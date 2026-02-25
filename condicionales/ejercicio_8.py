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