# Un alumno desea saber cual será su calificación final en la materia de Algoritmos
# Dicha calificación se compone de los siguientes porcentajes:
# * 55% del promedio de sus tres calificaciones parciales.
# * 30% de la calificación del examen final.
# * 15% de la calificación de un trabajo final.

parcial_1 = float(input("Ingrese la nota del 1er parcial: "))
parcial_2 = float(input("Ingrese la nota del 2do parcial: "))
parcial_3 = float(input("Ingrese la nota del 3er parcial: "))
examen_final = float(input("Ingrese la nota del examen final: "))
trabajo_final = float(input("Ingrese la nota del trabajo final: "))

calificacion_final = (parcial_1 * 0.20) + (parcial_2 * 0.20) + (parcial_3 * 0.20) + \
                     (examen_final * 0.20) + (trabajo_final * 0.20)

print("La calificación final del trabajo es:", calificacion_final)