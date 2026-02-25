<<<<<<< HEAD
# Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus ventas, 
# el vendedor desea saber cuanto dinero obtendrá por concepto de comisiones por 
# las tres ventas que realiza en el mes y el total que recibirá en el mes tomando 
# en cuenta su sueldo base y comisiones.

sueldo_base = float(input("Dime el sueldo base: "))
venta1 = float(input("Dame precio de la venta 1: "))
venta2 = float(input("Dame precio de la venta 2: "))
venta3 = float(input("Dime precio de la venta 3: "))

comision = (venta1 + venta2 + venta3) * 0.10

sueldo_total = sueldo_base + comision

print(f"Comisión por ventas: {comision}")
=======
# Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus ventas, 
# el vendedor desea saber cuanto dinero obtendrá por concepto de comisiones por 
# las tres ventas que realiza en el mes y el total que recibirá en el mes tomando 
# en cuenta su sueldo base y comisiones.

sueldo_base = float(input("Dime el sueldo base: "))
venta1 = float(input("Dame precio de la venta 1: "))
venta2 = float(input("Dame precio de la venta 2: "))
venta3 = float(input("Dime precio de la venta 3: "))

comision = (venta1 + venta2 + venta3) * 0.10

sueldo_total = sueldo_base + comision

print(f"Comisión por ventas: {comision}")
>>>>>>> 6f04b8a318105d39355a757f04fc5f7f571cb38c
print(f"Sueldo total: {sueldo_total}")