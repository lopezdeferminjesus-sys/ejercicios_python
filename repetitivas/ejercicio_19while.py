opcion = 0

while opcion != 5:
    
    print("\nMenú de recomendaciones")
    print("1. Literatura")
    print("2. Cine")
    print("3. Música")
    print("4. Videojuegos")
    print("5. Salir")
    
    opcion = int(input("Elija una opción (1-5): "))
    
    if opcion == 1:
        print("Lecturas recomendables:")
        print("+ Esperándolo a Tito")
        print("+ El juego de Ender")
        print("+ El sueño de los héroes")
        
    elif opcion == 2:
        print("Películas recomendables:")
        print("+ Matrix")
        print("+ El último samurái")
        print("+ Cars")
        
    elif opcion == 3:
        print("Discos recomendables:")
        print("+ Despedazado por mil partes")
        print("+ Búfalo")
        print("+ Gaia")
        
    elif opcion == 4:
        print("Videojuegos recomendables:")
        print("+ Día del tentáculo")
        print("+ Terminal Velocity")
        print("+ Death Rally")
        
    elif opcion == 5:
        print("Gracias, vuelva pronto")
        
    else:
        print("Opción no válida")