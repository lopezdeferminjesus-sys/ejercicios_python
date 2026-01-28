# Condicionales con Python
# if , else , elif

"""
if rxp_bool:
	instrucciones

if exp_bool:
	instrucciones 
	else:
		intrucciones 
		if exp_bool:
			instrucciones
			elif expo_bool:
				else:
					instrucciones

	"""


print('Inicio')

num = int(input('Ingresa un numero'))

if num > 0:
	print('Es un numero positivo')
elif num == 0:
	print('Es Cero')
else:
	print('No es un numero positivo')

print('Fin')



