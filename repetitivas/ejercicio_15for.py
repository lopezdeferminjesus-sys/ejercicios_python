pago = 10
pago_acum = 0

for mes in range(1, 21):
    print("Mes", mes, "- Pago:", pago)
    
    pago_acum = pago_acum + pago
    pago = pago * 2

print("Total pagado después de 20 meses:", pago_acum)