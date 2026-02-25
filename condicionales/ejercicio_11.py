ladoA = float(input("Introduce longitud lado A: "))
ladoB = float(input("Introduce longitud lado B: "))
ladoC = float(input("Introduce longitud lado C: "))

# Pitágoras (cualquier lado puede ser la hipotenusa)
if (ladoA**2 + ladoB**2 == ladoC**2) or (ladoB**2 + ladoC**2 == ladoA**2) or (ladoC**2 + ladoA**2 == ladoB**2):
    print("Triángulo Rectángulo")

# Isósceles
if (ladoA == ladoB and ladoA != ladoC) or (ladoB == ladoC and ladoB != ladoA) or (ladoC == ladoA and ladoC != ladoB):
    print("Triángulo Isósceles")
else:
    # Equilátero
    if ladoA == ladoB and ladoA == ladoC:
        print("Triángulo Equilátero")
    else:
        print("Triángulo Escaleno")