import matplotlib.pyplot as plt
from matplotlib. patches import Circle
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
def hacer_circulo():
    print("Haciendo circulo en 3D:")
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    r = 1
    phi = np.linspace(0, np.pi, 50)
    theta = np.linspace(0, 2*np.pi, 50)

    phi, theta = np.meshgrid(phi, theta)

    x = r * np.sin(phi) * np.cos(theta)
    y = r * np.sin(phi) * np.sin(theta)
    z = r * np.cos(phi)

    ax.plot_surface(x, y, z, color='lightblue', edgecolor='black', linewidth=0.5, alpha=0.9)

    ax.set_box_aspect([1,1,1])
    ax.set_xlim([-1.2, 1.2])
    ax.set_ylim([-1.2, 1.2])
    ax.set_zlim([-1.2, 1.2])

    ax.axis('on')  
    plt.title("Circulo 3D")

    plt.show()
    # print("Haciendo Circulo")
    # fig, ax = plt.subplots()

    # circulo = Circle((0.5, 0.5),0.2, color='blue', fill=True)

    # ax.add_patch(circulo)

    # ax.set_xlim(0, 1)
    # ax.set_ylim(0, 1)

    # ax.set_aspect('equal')

    # plt.show()

def hacer_cuadrado():
    print("Haciendo Cuadrado")
    print("Haciendo Cuadrado")
    x = [0, 2, 2, 0]
    y = [0, 0, 2, 2]

    plt.fill(x, y, color='blue')

    plt.gca().set_aspect('equal')

    plt.title("Cuadrado relleno con matplotlib")

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
    print("haciendo rombo")
    fig = plt.figure(figsize=(9, 7), facecolor='#0a0a1a')
    ax = fig.add_subplot(111, projection='3d', facecolor='#0a0a1a')

    # Vértices del rombo (4 puntos, figura plana en 3D)
    vertices = np.array([
        [ 0,  1.4,  0],   # arriba
        [ 1,  0,    0],   # derecha
        [ 0, -1.4,  0],   # abajo
        [-1,  0,    0],   # izquierda
    ])

    # Cara del rombo
    cara = [[vertices[0], vertices[1], vertices[2], vertices[3]]]

    fc = Poly3DCollection(cara, alpha=0.6, linewidths=2.5, edgecolors='#00eaff')
    fc.set_facecolor('#0044cc')
    ax.add_collection3d(fc)

    # Aristas
    for a, b in [(0,1),(1,2),(2,3),(3,0)]:
        ax.plot([vertices[a][0], vertices[b][0]],
                [vertices[a][1], vertices[b][1]],
                [vertices[a][2], vertices[b][2]],
                color='#00eaff', linewidth=2.5)

    # Diagonales punteadas
    for a, b in [(0,2),(1,3)]:
        ax.plot([vertices[a][0], vertices[b][0]],
                [vertices[a][1], vertices[b][1]],
                [vertices[a][2], vertices[b][2]],
                color='white', linewidth=1, linestyle='--', alpha=0.4)

    # Vértices
    ax.scatter(vertices[:,0], vertices[:,1], vertices[:,2],
            color='white', s=80, zorder=5)

    # Etiquetas
    nombres = ['A', 'B', 'C', 'D']
    offsets = [(0, 0.15, 0), (0.15, 0, 0), (0, -0.15, 0), (-0.18, 0, 0)]
    for i, (n, off) in enumerate(zip(nombres, offsets)):
        ax.text(vertices[i][0]+off[0], vertices[i][1]+off[1], vertices[i][2]+off[2],
                n, color='white', fontsize=12, fontweight='bold')

    # Estilo
    ax.set_xlim([-1.8, 1.8])
    ax.set_ylim([-1.8, 1.8])
    ax.set_zlim([-1, 1])
    ax.set_xlabel('X', color='#aaaaff')
    ax.set_ylabel('Y', color='#aaaaff')
    ax.set_zlabel('Z', color='#aaaaff')
    ax.tick_params(colors='#555577')
    ax.xaxis.pane.fill = False
    ax.yaxis.pane.fill = False
    ax.zaxis.pane.fill = False
    ax.xaxis.pane.set_edgecolor('#1a1a3a')
    ax.yaxis.pane.set_edgecolor('#1a1a3a')
    ax.zaxis.pane.set_edgecolor('#1a1a3a')
    ax.grid(True, color='#1a1a3a', linewidth=0.5)
    ax.set_title('Rombo en 3D', color='#00eaff', fontsize=16,
                fontweight='bold', pad=18)
    ax.view_init(elev=30, azim=45)

    plt.tight_layout()
    plt.show()
def hacer_Rectangulo():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # vertices del prisma rectangular
    x = [0, 3, 3, 0, 0, 3, 3, 0]
    y = [0, 0, 2, 2, 0, 0, 2, 2]
    z = [0, 0, 0, 0, 2, 2, 2, 2]

    # lineas que conectan los puntos
    edges = [
        [0,1],[1,2],[2,3],[3,0],  # base
        [4,5],[5,6],[6,7],[7,4],  # arriba
        [0,4],[1,5],[2,6],[3,7]   # verticales
    ]

    for edge in edges:
        ax.plot([x[edge[0]], x[edge[1]]],
                [y[edge[0]], y[edge[1]]],
                [z[edge[0]], z[edge[1]]])

    ax.set_title("Rectangulo 3D")
    plt.show()

def menu():
    print("Menu de figuras geometricas")
while True:
    menu()
    try:
        print( "Bienvenido ")
        opcion = int(input(" seleccione la figura que desee hacer \n 1. un circulo \n 2. un cuadrado \n 3. un triangulo  \n  4. un rombo \n 5. rectangulo \n 6. salir \n "))
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
                hacer_Rectangulo()
            case 6:
                print("haz elegido salir")
                break 
            case _: 
                print("esta opcion no esta en el menu, porfavor elegir algo del menu")
                continue 
    except ValueError:
        print(" No se pueden usar letras porfavor digite el numero que esta en pantallaza ")
        