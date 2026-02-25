"""
//El director de una escuela está organizando un viaje de estudios, y requiere 
//determinar cuánto debe cobrar a cada alumno y cuánto debe pagar a la compañía de 
//viajes por el servicio. La forma de cobrar es la siguiente: 
//si son 100 alumnos o más, el costo por cada alumno es de 65 euros; 
//de 50 a 99 alumnos, el costo es de 70 euros, de 30 a 49, de 95 euros, 
//y si son menos de 30, el costo de la renta del autobús es de 4000 euros, 
//sin importar el número de alumnos. 
//Realice un algoritmo que permita determinar el pago a la compañía de autobuses 
//y lo que debe pagar cada alumno por el viaje.
"""


tiempo = int(input("¿Cuánto tiempo es la llamada?: "))
es_domingo = input("¿Es Domingo? (S/N): ")

if es_domingo.upper() == "N":
    turno = input("¿Qué turno: Mañana o Tarde? (M/T)?: ")

# Cálculo del coste base en céntimos
if tiempo < 5:
    coste = tiempo * 100
else:
    if tiempo < 8:
        coste = (tiempo - 5) * 80 + 500
    else:
        if tiempo < 10:
            coste = (tiempo - 8) * 70 + 240 + 500
        else:
            coste = (tiempo - 10) * 50 + 140 + 240 + 500

# Aplicación de impuesto
if es_domingo.upper() == "S":
    coste = coste + coste * 0.03
else:
    if turno.upper() == "M":
        coste = coste + coste * 0.15
    else:
        coste = coste + coste * 0.10

print("El coste de la llamada:", coste / 100, "euros.")