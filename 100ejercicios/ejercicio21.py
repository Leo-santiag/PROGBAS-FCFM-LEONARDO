import math
def esfera():
    radio = float(input("Introduce el radio de la esfera: "))
    volumen = (4/3) * math.pi * (radio ** 3)
    area = 4 * math.pi * (radio ** 2)
    print(f"Volumen de la esfera: {volumen:.2f}")
    print(f"Área de la superficie de la esfera: {area:.2f}")

def cubo():
    lado = float(input("Introduce el lado del cubo: "))
    volumen = lado ** 3
    area = 6 * (lado ** 2)
    print(f"Volumen del cubo: {volumen:.2f}")
    print(f"Área de la superficie del cubo: {area:.2f}")

def cilindro():
    radio = float(input("Introduce el radio de la base del cilindro: "))
    altura = float(input("Introduce la altura del cilindro: "))
    volumen = math.pi * (radio ** 2) * altura
    area = 2 * math.pi * radio * (radio + altura)
    print(f"Volumen del cilindro: {volumen:.2f}")
    print(f"Área de la superficie del cilindro: {area:.2f}")

def cono():
    radio = float(input("Introduce el radio de la base del cono: "))
    altura = float(input("Introduce la altura del cono: "))
    volumen = (1/3) * math.pi * (radio ** 2) * altura
    area = math.pi * radio * (radio + math.sqrt(altura ** 2 + radio ** 2))
    print(f"Volumen del cono: {volumen:.2f}")
    print(f"Área de la superficie del cono: {area:.2f}")

def prismarectangular():
    largo = float(input("Introduce el largo del prisma rectangular: "))
    ancho = float(input("Introduce el ancho del prisma rectangular: "))
    altura = float(input("Introduce la altura del prisma rectangular: "))
    volumen = largo * ancho * altura
    area = 2 * (largo * ancho + largo * altura + ancho * altura)
    print(f"Volumen del prisma rectangular: {volumen:.2f}")
    print(f"Área de la superficie del prisma rectangular: {area:.2f}")

def prismatriangular():
    base = float(input("Introduce la base del prisma triangular: "))
    altura = float(input("Introduce la altura del prisma triangular: "))
    longitud = float(input("Introduce la longitud del prisma triangular: "))
    volumen = 0.5 * base * altura * longitud
    area = base * altura + 3 * (base * longitud) / 2
    print(f"Volumen del prisma triangular: {volumen:.2f}")
    print(f"Área de la superficie del prisma triangular: {area:.2f}")

def tetraedro():
    lado = float(input("Introduce el lado del tetraedro: "))
    volumen = (lado ** 3) / (6 * math.sqrt(2))
    area = math.sqrt(3) * (lado ** 2)
    print(f"Volumen del tetraedro: {volumen:.2f}")
    print(f"Área de la superficie del tetraedro: {area:.2f}")

def octaedro():
    lado = float(input("Introduce el lado del octaedro: "))
    volumen = (math.sqrt(2) / 3) * (lado ** 3)
    area = 2 * math.sqrt(3) * (lado ** 2)
    print(f"Volumen del octaedro: {volumen:.2f}")
    print(f"Área de la superficie del octaedro: {area:.2f}")

def dodecaedro():
    lado = float(input("Introduce el lado del dodecaedro: "))
    volumen = (15 + 7 * math.sqrt(5)) / 4 * (lado ** 3)
    area = 3 * math.sqrt(25 + 10 * math.sqrt(5)) * (lado ** 2)
    print(f"Volumen del dodecaedro: {volumen:.2f}")
    print(f"Área de la superficie del dodecaedro: {area:.2f}")

def icosaedro():
    lado = float(input("Introduce el lado del icosaedro: "))
    volumen = (5 * (3 + math.sqrt(5)) / 12) * (lado ** 3)
    area = 5 * math.sqrt(3) * (lado ** 2)
    print(f"Volumen del icosaedro: {volumen:.2f}")
    print(f"Área de la superficie del icosaedro: {area:.2f}")
def circulo():
    radio = float(input("Introduce el radio del círculo: "))
    area = math.pi * (radio ** 2)
    print(f"El área del círculo es: {area:.2f}")

def triangulo():
    base = float(input("Introduce la base del triángulo: "))
    altura = float(input("Introduce la altura del triángulo: "))
    area = 0.5 * base * altura
    print(f"El área del triángulo es: {area:.2f}")

def cuadrado():
    lado = float(input("Introduce el lado del cuadrado: "))
    area = lado ** 2
    print(f"El área del cuadrado es: {area:.2f}")

def rectangulo():
    base = float(input("Introduce la base del rectángulo: "))
    altura = float(input("Introduce la altura del rectángulo: "))
    area = base * altura
    print(f"El área del rectángulo es: {area:.2f}")

def pentagono():
    lado = float(input("Introduce el lado del pentágono: "))
    apotema = float(input("Introduce el apotema del pentágono: "))
    perimetro = 5 * lado
    area = (perimetro * apotema) / 2
    print(f"El área del pentágono es: {area:.2f}")

def hexagono():
    lado = float(input("Introduce el lado del hexágono: "))
    apotema = float(input("Introduce el apotema del hexágono: "))
    perimetro = 6 * lado
    area = (perimetro * apotema) / 2
    print(f"El área del hexágono es: {area:.2f}")

def heptagono():
    lado = float(input("Introduce el lado del heptágono: "))
    apotema = float(input("Introduce el apotema del heptágono: "))
    perimetro = 7 * lado
    area = (perimetro * apotema) / 2
    print(f"El área del heptágono es: {area:.2f}")

def octagono():
    lado = float(input("Introduce el lado del octágono: "))
    apotema = float(input("Introduce el apotema del octágono: "))
    perimetro = 8 * lado
    area = (perimetro * apotema) / 2
    print(f"El área del octágono es: {area:.2f}")

def trapecio():
    base_mayor = float(input("Introduce la base mayor del trapecio: "))
    base_menor = float(input("Introduce la base menor del trapecio: "))
    altura = float(input("Introduce la altura del trapecio: "))
    area = ((base_mayor + base_menor) / 2) * altura
    print(f"El área del trapecio es: {area:.2f}")

def rombo():
    diagonal_mayor = float(input("Introduce la diagonal mayor del rombo: "))
    diagonal_menor = float(input("Introduce la diagonal menor del rombo: "))
    area = (diagonal_mayor * diagonal_menor) / 2
    print(f"El área del rombo es: {area:.2f}")
def menu_figuras3D():
    figuras3D = """
    Elija una figura en 3D
    >>> (1) Esfera
    >>> (2) Cubo
    >>> (3) Cilindro
    >>> (4) Cono
    >>> (5) Prisma Rectangular
    >>> (6) Prisma Triangular
    >>> (7) Tetraedro
    >>> (8) Octaedro
    >>> (9) Dodecaedro
    >>> (10) Icosaedro
    """
    print(figuras3D)
    return int(input())

def menu_figuras():
    figuras = """
    Elija una figura 
    >>>(1)Círculo
    >>>(2)Triángulo
    >>>(3)Cuadrado
    >>>(4)Rectángulo
    >>>(5)Pentágono
    >>>(6)Hexágono
    >>>(7)Heptágono
    >>>(8)Octágono
    >>>(9)Trapecio
    >>>(10)Rombo
    """
    print(figuras)
    return int(input())
     

def mostrar_menu():
    menu = """
    Bienvenido al menú
    Calcular área y volumen de distintas figuras geométricas
    Inicio 
    >>> Elija entre las opciones 
    >>> (1)Dos dimensiones 
    >>> (2)Tres dimensiones 
    """
    print(menu)
    return int(input())

opcion_uno = mostrar_menu()

while (opcion_uno != 1) and (opcion_uno != 2):
    print("Seleccione una opción correcta")
    opcion_uno = mostrar_menu()

if opcion_uno == 1:
    figuraelegida = menu_figuras()
    while (figuraelegida !=1)and(figuraelegida!=2)and(figuraelegida !=3)and(figuraelegida!=4)and(figuraelegida !=5)and(figuraelegida!=6)and(figuraelegida !=7)and(figuraelegida!=8)and(figuraelegida !=9)and(figuraelegida!=10):
        print("Eleja una de las opiones disponibles") 
        figuraelegida = menu_figuras()
    if figuraelegida == 1:
        circulo()
    elif figuraelegida == 2:
        triangulo()
    elif figuraelegida == 3:
        cuadrado()
    elif figuraelegida == 4:
        rectangulo()
    elif figuraelegida == 5:
        pentagono()
    elif figuraelegida == 6:
        hexagono()
    elif figuraelegida == 7:
        heptagono()
    elif figuraelegida == 8:
        octagono()
    elif figuraelegida == 9:
        trapecio()
    elif figuraelegida == 10:
        rombo()
    else:
        print("no es posible imprimir este mensaje gracias a las validaciones")

if opcion_uno == 2:
    figura3Delegida = menu_figuras3D()
    while (figura3Delegida !=1)and(figura3Delegida!=2)and(figura3Delegida !=3)and(figura3Delegida!=4)and(figura3Delegida !=5)and(figura3Delegida!=6)and(figura3Delegida !=7)and(figura3Delegida!=8)and(figura3Delegida !=9)and(figura3Delegida!=10):
        print("Eleja una de las opiones disponibles") 
        figuraelegida = menu_figuras3D()
    if figura3Delegida == 1:
        esfera()
    elif figura3Delegida == 2:
        cubo()
    elif figura3Delegida == 3:
        cilindro()
    elif figura3Delegida == 4:
        cono()
    elif figura3Delegida == 5:
        prismarectangular()
    elif figura3Delegida == 6:
        prismatriangular()
    elif figura3Delegida == 7:
        tetraedro()
    elif figura3Delegida == 8:
        octaedro()
    elif figura3Delegida == 9:
        dodecaedro()
    elif figura3Delegida == 10:
        icosaedro()
    else:
        print("no es posible imprimir este mensaje gracias a las validaciones")

