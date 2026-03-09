def hacer_circulo():
    print("haciendo un circulo")
def hacer_cuadrado():
    print("haciendo un cuadrado")
def hacer_triangulo():
    print("haciendo triangulo")
def hacer_rombo():
    print("haciendo rombo")
def menu():
    print("Menu de figuras geometricas")
while True:
    menu()
    try:
        print( "Bienvenido ")
        opcion = int(input(" seleccione la figura que desee hacer \n 1. un circulo \n 2. un cuadrado \n 3. un triangulo \n  4. un rombo \n 5. salir \n "))
        match opcion: 
            case 1:
                hacer_circulo()
            case 2:
                hacer_cuadrado()
            case 3: 
                hacer_triangulo()
            case 4:
                hacer_rombo()
            case 5:
                print("Haz elejido salir ")
                break
            case _: 
                print("esta opcion no esta en el menu, porfavor elegir algo del menu")
                continue 
    except ValueError:
        print(" No se pueden usar letras porfavor digite el numero que esta en pantallaza ")
        