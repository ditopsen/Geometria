import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# ── funciones de cálculo con return ──
def calcular_circulo(r):
    area = round(np.pi * r**2, 4)
    perimetro = round(2 * np.pi * r, 4)
    return area, perimetro

def calcular_cuadrado(lado):
    area = round(lado**2, 4)
    perimetro = round(4 * lado, 4)
    return area, perimetro
def calcular_triangulo(base, altura):
    lado_lat = round(np.sqrt((base/2)**2 + altura**2), 4)
    area = round((base * altura) / 2, 4)
    perimetro = round(base + 2 * lado_lat, 4)
    return area, perimetro

def calcular_rombo(d1, d2):
    area = round((d1 * d2) / 2, 4)
    lado = round(np.sqrt((d1/2)**2 + (d2/2)**2), 4)
    perimetro = round(4 * lado, 4)
    return area, perimetro

def calcular_rectangulo(largo, ancho):
    area = round(largo * ancho, 4)
    perimetro = round(2 * (largo + ancho), 4)
    return area, perimetro

# ── label centrado con annotate ──
def label_centro_2d(ax, cx, cy, area, perimetro):
    label = f"Área = {area}\nPerímetro = {perimetro}"
    ax.annotate(label, xy=(cx, cy),
                fontsize=10,
                ha='center', va='center',
                bbox=dict(boxstyle='round', facecolor='#ffffcc', alpha=0.8))

def label_centro_3d(ax, area, perimetro):
    label = f"Área = {area}\nPerímetro = {perimetro}"
    ax.text2D(0.5, 0.5, label,
            transform=ax.transAxes,
            fontsize=10,
            ha='center', va='center',
            bbox=dict(boxstyle='round', facecolor='#ffffcc', alpha=0.8))

# ── figuras ──
def hacer_circulo():
    print("Haciendo circulo en 3D:")

    r = float(input("Ingresa el radio del circulo: "))
    area, perimetro = calcular_circulo(r)
    print(f"  Área      = {area}")
    print(f"  Perímetro = {perimetro}")     

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    phi = np.linspace(0, np.pi, 50)
    theta = np.linspace(0, 2*np.pi, 50)
    phi, theta = np.meshgrid(phi, theta)

    x = r * np.sin(phi) * np.cos(theta)
    y = r * np.sin(phi) * np.sin(theta)
    z = r * np.cos(phi)

    ax.plot_surface(x, y, z, color='lightblue', edgecolor='black', linewidth=0.5, alpha=0.9)
    ax.set_box_aspect([1,1,1])
    ax.set_xlim([-r*1.2, r*1.2])
    ax.set_ylim([-r*1.2, r*1.2])
    ax.set_zlim([-r*1.2, r*1.2])
    ax.axis('on')
    label_centro_3d(ax, area, perimetro)
    plt.title("Circulo 3D")
    plt.show()

def hacer_circulo_2d():
    print("Haciendo circulo en 2D:")

    r = float(input("Ingresa el radio del circulo: "))
    area, perimetro = calcular_circulo(r)
    print(f"  Área      = {area}")
    print(f"  Perímetro = {perimetro}")

    fig, ax = plt.subplots()
    circulo = Circle((0, 0), r, color='lightblue', fill=True, linewidth=2, edgecolor='black')
    ax.add_patch(circulo)
    ax.set_xlim([-r*1.5, r*1.5])
    ax.set_ylim([-r*1.5, r*1.5])
    ax.set_aspect('equal')
    label_centro_2d(ax, 0, 0, area, perimetro)
    plt.title("Circulo 2D")
    plt.show()

def hacer_cuadrado():
    print("Haciendo Cuadrado")
    print("Haciendo Cuadrado")

    lado = float(input("Ingresa el lado del cuadrado: "))
    area, perimetro = calcular_cuadrado(lado)
    print(f"  Área      = {area}")
    print(f"  Perímetro = {perimetro}")

    fig, ax = plt.subplots()
    x = [0, lado, lado, 0]
    y = [0, 0, lado, lado]
    ax.fill(x, y, color='blue')
    ax.set_aspect('equal')
    label_centro_2d(ax, lado/2, lado/2, area, perimetro)
    plt.title("Cuadrado relleno con matplotlib")
    plt.show()

def hacer_cuadrado_3d():
    print("Haciendo Cuadrado en 3D (Cubo)")

    lado = float(input("Ingresa el lado del cuadrado: "))
    area = round(6 * lado**2, 4)
    perimetro = round(4 * lado, 4)
    print(f"  Área superficial = {area}")
    print(f"  Perímetro cara   = {perimetro}")

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    r = [0, lado]
    vertices = np.array([[x, y, z] for x in r for y in r for z in r])
    caras = [
        [vertices[i] for i in [0,1,3,2]],
        [vertices[i] for i in [4,5,7,6]],
        [vertices[i] for i in [0,1,5,4]],
        [vertices[i] for i in [2,3,7,6]],
        [vertices[i] for i in [0,2,6,4]],
        [vertices[i] for i in [1,3,7,5]],
    ]
    poly = Poly3DCollection(caras, alpha=0.4, linewidths=1, edgecolors='black')
    poly.set_facecolor('royalblue')
    ax.add_collection3d(poly)
    ax.set_xlim([0, lado]); ax.set_ylim([0, lado]); ax.set_zlim([0, lado])
    label_centro_3d(ax, area, perimetro)
    plt.title("Cuadrado 3D (Cubo)")
    plt.show()

def hacer_triangulo():
    base = float(input("Ingresa la base del triángulo: "))
    altura = float(input("Ingresa la altura del triángulo: "))
    area, perimetro = calcular_triangulo(base, altura)
    print(f"  Área      = {area}")
    print(f"  Perímetro = {perimetro}")

    fig, ax = plt.subplots()

    x = [-base/2, base/2, 0, -base/2]
    y = [0, 0, altura, 0]

    ax.plot(x, y)
    ax.fill(x[:-1], y[:-1], color='lightcoral', alpha=0.6)
    # centroide del triángulo
    cx = 0
    cy = altura / 3
    label_centro_2d(ax, cx, cy, area, perimetro)
    ax.set_aspect('equal')
    ax.set_xlim(-base*0.8, base*0.8)
    ax.set_ylim(-altura*0.3, altura*1.3)
    plt.title("Triangulo")
    plt.show()
    print("haciendo triangulo")

def hacer_triangulo_3d():
    print("Haciendo Triangulo en 3D (Pirámide)")

    base = float(input("Ingresa la base del triángulo: "))
    altura = float(input("Ingresa la altura: "))
    area_base = round((np.sqrt(3)/4) * base**2, 4)
    volumen = round((1/3) * area_base * altura, 4)
    print(f"  Área base  = {area_base}")
    print(f"  Volumen    = {volumen}")

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    base_v = np.array([[base,0,0], [-base,0,0], [0,base*1.5,0]])
    apice  = np.array([0, base*0.5, altura])
    caras = [
        [base_v[0], base_v[1], base_v[2]],
        [base_v[0], base_v[1], apice],
        [base_v[1], base_v[2], apice],
        [base_v[0], base_v[2], apice],
    ]
    poly = Poly3DCollection(caras, alpha=0.7, linewidths=1.5, edgecolors='darkred')
    poly.set_facecolor(['#ff7755','#ff9977','#ff5533','#ffbb99'])
    ax.add_collection3d(poly)
    lim = base*1.8
    ax.set_xlim([-lim, lim]); ax.set_ylim([-0.5, lim]); ax.set_zlim([0, altura*1.2])
    label_centro_3d(ax, area_base, volumen)
    ax.set_xlabel('X'); ax.set_ylabel('Y'); ax.set_zlabel('Z')
    plt.title("Triangulo 3D (Pirámide)")
    plt.show()

def hacer_rombo():
    print("haciendo rombo")

    d1 = float(input("Ingresa la diagonal mayor (D): "))
    d2 = float(input("Ingresa la diagonal menor (d): "))
    area, perimetro = calcular_rombo(d1, d2)
    print(f"  Área      = {area}")
    print(f"  Perímetro = {perimetro}")

    fig = plt.figure(figsize=(9, 7), facecolor='#0a0a1a')
    ax = fig.add_subplot(111, projection='3d', facecolor='#0a0a1a')

    vertices = np.array([
        [ 0,  d1/2,  0],
        [ d2/2,  0,  0],
        [ 0, -d1/2,  0],
        [-d2/2,  0,  0],
    ])

    cara = [[vertices[0], vertices[1], vertices[2], vertices[3]]]
    fc = Poly3DCollection(cara, alpha=0.6, linewidths=2.5, edgecolors='#00eaff')
    fc.set_facecolor('#0044cc')
    ax.add_collection3d(fc)

    for a, b in [(0,1),(1,2),(2,3),(3,0)]:
        ax.plot([vertices[a][0], vertices[b][0]],
                [vertices[a][1], vertices[b][1]],
                [vertices[a][2], vertices[b][2]],
                color='#00eaff', linewidth=2.5)

    for a, b in [(0,2),(1,3)]:
        ax.plot([vertices[a][0], vertices[b][0]],
                [vertices[a][1], vertices[b][1]],
                [vertices[a][2], vertices[b][2]],
                color='white', linewidth=1, linestyle='--', alpha=0.4)

    ax.scatter(vertices[:,0], vertices[:,1], vertices[:,2], color='white', s=80, zorder=5)

    nombres = ['A', 'B', 'C', 'D']
    offsets = [(0, 0.15, 0), (0.15, 0, 0), (0, -0.15, 0), (-0.18, 0, 0)]
    for i, (n, off) in enumerate(zip(nombres, offsets)):
        ax.text(vertices[i][0]+off[0], vertices[i][1]+off[1], vertices[i][2]+off[2],
                n, color='white', fontsize=12, fontweight='bold')

    label_centro_3d(ax, area, perimetro)

    lim = max(d1, d2) * 0.7
    ax.set_xlim([-lim, lim]); ax.set_ylim([-lim, lim]); ax.set_zlim([-1, 1])
    ax.set_xlabel('X', color='#aaaaff'); ax.set_ylabel('Y', color='#aaaaff')
    ax.set_zlabel('Z', color='#aaaaff')
    ax.tick_params(colors='#555577')
    ax.xaxis.pane.fill = False; ax.yaxis.pane.fill = False; ax.zaxis.pane.fill = False
    ax.xaxis.pane.set_edgecolor('#1a1a3a')
    ax.yaxis.pane.set_edgecolor('#1a1a3a')
    ax.zaxis.pane.set_edgecolor('#1a1a3a')
    ax.grid(True, color='#1a1a3a', linewidth=0.5)
    ax.set_title('Rombo en 3D', color="#32cad8", fontsize=16, fontweight='bold', pad=18)
    ax.view_init(elev=30, azim=45)
    plt.tight_layout()
    plt.show()

def hacer_rombo_2d():
    print("haciendo rombo 2D")

    d1 = float(input("Ingresa la diagonal mayor (D): "))
    d2 = float(input("Ingresa la diagonal menor (d): "))
    area, perimetro = calcular_rombo(d1, d2)
    print(f"  Área      = {area}")
    print(f"  Perímetro = {perimetro}")

    fig, ax = plt.subplots()
    from matplotlib.patches import Polygon as MplPolygon
    rombo = MplPolygon([[0, d1/2],[d2/2, 0],[0, -d1/2],[-d2/2, 0]],
                        closed=True, color='mediumslateblue', alpha=0.8,
                        edgecolor='indigo', linewidth=2)
    ax.add_patch(rombo)
    ax.plot([0,0],[d1/2,-d1/2],'w--', alpha=0.5, linewidth=1)
    ax.plot([-d2/2,d2/2],[0,0],'w--', alpha=0.5, linewidth=1)
    lim = max(d1, d2) * 0.7
    ax.set_xlim([-lim, lim]); ax.set_ylim([-lim, lim])
    ax.set_aspect('equal')
    # centro del rombo es (0, 0)
    label_centro_2d(ax, 0, 0, area, perimetro)
    plt.title("Rombo 2D")
    plt.show()

def hacer_Rectangulo():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    largo = float(input("Ingresa el largo del rectángulo: "))
    ancho = float(input("Ingresa el ancho del rectángulo: "))
    area, perimetro = calcular_rectangulo(largo, ancho)
    print(f"  Área      = {area}")
    print(f"  Perímetro = {perimetro}")

    x = [0, largo, largo, 0, 0, largo, largo, 0]
    y = [0, 0, ancho, ancho, 0, 0, ancho, ancho]
    z = [0, 0, 0, 0, ancho, ancho, ancho, ancho]

    edges = [
        [0,1],[1,2],[2,3],[3,0],
        [4,5],[5,6],[6,7],[7,4],
        [0,4],[1,5],[2,6],[3,7]
    ]

    for edge in edges:
        ax.plot([x[edge[0]], x[edge[1]]],
                [y[edge[0]], y[edge[1]]],
                [z[edge[0]], z[edge[1]]])

    label_centro_3d(ax, area, perimetro)
    ax.set_title("Rectangulo 3D")
    plt.show()

def hacer_Rectangulo_2d():
    print("Haciendo Rectangulo 2D")

    largo = float(input("Ingresa el largo del rectángulo: "))
    ancho = float(input("Ingresa el ancho del rectángulo: "))
    area, perimetro = calcular_rectangulo(largo, ancho)
    print(f"  Área      = {area}")
    print(f"  Perímetro = {perimetro}")

    x = [0, largo, largo, 0]
    y = [0, 0, ancho, ancho]

    fig, ax = plt.subplots()
    ax.fill(x, y, color='mediumseagreen')
    ax.set_aspect('equal')
    # centro geométrico del rectángulo
    label_centro_2d(ax, largo/2, ancho/2, area, perimetro)
    plt.title("Rectangulo 2D")
    plt.show()

def menu():
    print("Menu de figuras geometricas")

while True:
    menu()
    try:
        print("Bienvenido ")
        opcion = int(input(" seleccione la figura que desee hacer \n 1. un circulo 3D \n 2. un circulo 2D \n 3. un cuadrado \n 4. un cuadrado 3D \n 5. un triangulo \n 6. un triangulo 3D \n 7. un rombo 3D \n 8. un rombo 2D \n 9. rectangulo 3D \n 10. rectangulo 2D \n 11. salir \n "))
        match opcion:
            case 1:
                hacer_circulo()
            case 2:
                hacer_circulo_2d()
            case 3:
                hacer_cuadrado()
            case 4:
                hacer_cuadrado_3d()
            case 5:
                hacer_triangulo()
            case 6:
                hacer_triangulo_3d()
            case 7:
                hacer_rombo()
            case 8:
                hacer_rombo_2d()
            case 9:
                hacer_Rectangulo()
            case 10:
                hacer_Rectangulo_2d()
            case 11:
                print("haz elegido salir")
                break
            case _:
                print("esta opcion no esta en el menu, porfavor elegir algo del menu")
                continue
    except ValueError:
        print(" No se pueden usar letras porfavor digite el numero que esta en pantallaza ")
        