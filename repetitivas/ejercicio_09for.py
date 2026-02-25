base = float(input("Dame la base de la potencia: "))
exponente = int(input("Dame el exponente de la potencia: "))

potencia = 1

for i in range(exponente):
    potencia = potencia * base

print("Potencia:", potencia)