car = input("Introduce un carácter: ")

while car != " ":
    
    if car == "A" or car == "E" or car == "I" or car == "O" or car == "U" or \
       car == "a" or car == "e" or car == "i" or car == "o" or car == "u":
        print("VOCAL")
    else:
        print("NO VOCAL")
    
    car = input("Introduce un carácter: ")