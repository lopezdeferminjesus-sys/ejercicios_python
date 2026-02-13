"""
Escribe un programa que pida una fecha (día, mes y año) y diga si es correcta.
"""


dia = int(input("Introduce el dia: "))
mes = int(input("Introduce el mes: "))
año = int(input("Introduce el año: "))

dias_del_mes = 0

if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    dias_del_mes = 31
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    dias_del_mes = 30
elif mes == 2:
    if (año % 4 == 0 and not (año % 100 == 0)) or (año % 400 == 0):
        dias_del_mes = 29
    else:
        dias_del_mes = 28
else:
    print("Fecha incorrecta")

if mes >= 1 and mes <= 12:
    if dia < 1 or dia > dias_del_mes:
        print("Fecha incorrecta")
    else:
        print("Fecha correcta")