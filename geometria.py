import matplotlib.pyplot as plt
from matplotlib. patches import Circle
def hacer_circulo():
    print("haciendo un circulo")
    fig, ax = plt.subplots()

    circulo = Circle((0, 0), 1, fill=False)  # (centro_x, centro_y), radio
    ax.add_patch(circulo)

    ax.set_aspect('equal')
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)

    plt.title("Círculo")
    plt.show()
def hacer_cuadrado():
    print("haciendo un cuadrado")
    fig, ax = plt.subplots()

    # coordenadas del cuadrado
    x = [-1, 1, 1, -1, -1]
    y = [-1, -1, 1, 1, -1]

    ax.plot(x, y)

    ax.set_aspect('equal')
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)

    plt.title("Cuadrado")
    plt.show()
def hacer_triangulo():
    fig, ax = plt.subplots()

    # coordenadas del triangulo
    x = [0, -1, 1, 0]
    y = [1, -1, -1, 1]

    ax.plot(x, y)

    ax.set_aspect('equal')
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)

    plt.title("Triangulo")
    plt.show()
    print("haciendo triangulo")
def hacer_rombo():
    fig, ax = plt.subplots()

    # coordenadas del rombo
    x = [0, 1, 0, -1, 0]
    y = [1, 0, -1, 0, 1]

    ax.plot(x, y)

    ax.set_aspect('equal')
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)

    plt.title("Rombo")
    plt.show()
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
        