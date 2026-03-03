while True:
    try:
        print( "Bienvenido ")
        opcion = (int(input(" seleccione la figura que desee hacer \n 1. un circulo \n 2. un cuadrado \n 3. un triangulo \n  4. un rombo \n 5. salir \n ")))
        match opcion: 
            case 1:
                print("ha elejido el circulo")
            case 2:
                print("ha elejido un cuadrado")
            case 3: 
                print(" ha elejido un triangulo")
            case 4:
                print("has elejido un rombo")
            case 5:
                print("Haz elejido salir ")
                break
    except ValueError:
        print(" No se pueden usar letras porfavor digite el numero que esta en pantallaza")
