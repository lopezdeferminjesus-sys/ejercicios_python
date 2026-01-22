# calcular el perimetro y area de un rectangulo dada su base y 

# input 




print("Calculo de Area y Perimetro de un Rectangulo")
base = input('ingresa la base: ')
base = int(base)

height = input ('ingresa la altura: ')
height = int(height)

area = base * height
perimeter = base + base + height + height

print("Area:", area)
print("Perimetro:", perimeter)