# Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente 
# desea saber cuanto deberá pagar finalmente por su compra.

precio = float(input("Dime el precio de la compra: "))

descuento = precio * 0.15

precio_final = precio - descuento

print("Precio final con descuento:", precio_final)