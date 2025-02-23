import time
def multiplicar_matrices(matriz1, matriz2):
    filas_m1 = len(matriz1)
    columnas_m1 = len(matriz1[0])
    columnas_m2 = len(matriz2[0])
    producto = []
    for i in range(filas_m1):
        fila = []
        for j in range(columnas_m2):
            suma = 0
            for k in range(columnas_m1):
                suma += matriz1[i][k] * matriz2[k][j]
            fila.append(suma)
        producto.append(fila)
    return producto
def multiplicar_constante_matriz(constante, matriz):
    resultado = []
    for fila in matriz:
        nueva_fila = []
        for elemento in fila:
            nueva_fila.append(constante * elemento)
        resultado.append(nueva_fila)
    return resultado
def crear_matriz(filas,columnas):

    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            valor = float(input(f"Introduce el valor para la posición ({i}, {j}): "))
            fila.append(valor)
        matriz.append(fila)
    return matriz
def restar_matrices(matriz1, matriz2):
    filas = len(matriz1)
    columnas = len(matriz1[0])
    resta = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(matriz1[i][j] - matriz2[i][j])
        resta.append(fila)
    return resta
def sumar_matrices(matriz1, matriz2):
    filas = len(matriz1)
    columnas = len(matriz1[0])
    suma = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(matriz1[i][j] + matriz2[i][j])
        suma.append(fila)
    return suma
def imprimir_matriz(matriz):
    for fila in matriz:
        print(" ".join(map(str, fila)))
def espera_con_mensaje(tiempo):
    print("Cargando...", end="", flush=True)
    for _ in range(tiempo):
        time.sleep(1)
        print(".", end="", flush=True)
    print("\nProceso completado.")
def menu():
    menu = """
    INICIO...
    >>>Calculadora de matrices jejeje 
    seleccione algun procedimiento para realizar... 
    ---(1)Sumar matrices >>> solo funciona esta
    ---(2)Restar matrices >>> esta tanbien 
    ---(3)Multiplicar matrices 
    ---(4)Multiplicar una matriz por una constante 
    ---(5)Encontrar el determinante (no sirve) 
    ---(6)Hallar la inversa (en mantenimiento) 
    ---(7)reducir una matriz a diagonal (en mantenimieto) 
    """
    print(menu)
    return int(input())
opc_1 = menu()
while (opc_1 != 1)and(opc_1 != 2)and(opc_1 != 3)and(opc_1 != 4)and(opc_1 != 5)and(opc_1 != 6)and(opc_1 != 7): 
    print("Elija una de las opciones disponibles")
    opc_1=menu()
if opc_1 == 1:
    print("usted encontrara A+B")
    print("Por lo tanto las matrices tienen que tener dimencsiones iguales (nxn)+(nxn)")
    filas_1 = int(input("Introduce el número de filas para la Matriz 1 (A): "))
    columnas_1 = int(input("Introduce el número de columnas para la Matriz 1 (A): "))
    filas_2 = int(input("Introduce el número de filas para la Matriz 2 (B): "))
    columnas_2 = int(input("Introduce el número de columnas para la Matriz 2 (B): "))
    while (filas_1!=filas_2)and(columnas_1!=columnas_2):
        print("Dimenciones distintas Pruebe denuevo ingresar los datos")
        print("usted encontrara A+B")
        print("Por lo tanto las matrices tienen que tener dimencsiones iguales")
        filas_1 = int(input("Introduce el número de filas para la Matriz 1 (A): "))
        columnas_1 = int(input("Introduce el número de columnas para la Matriz 1 (A): "))
        filas_2 = int(input("Introduce el número de filas para la Matriz 2 (B): "))
        columnas_2 = int(input("Introduce el número de columnas para la Matriz 2 (B): "))
        
    Matriz_1 = crear_matriz(filas_1,columnas_1)
    imprimir_matriz(Matriz_1)
    Matriz_2 = crear_matriz(filas_2,columnas_2)
    imprimir_matriz(Matriz_2)
    sumamatriz = sumar_matrices(Matriz_1,Matriz_2)
    espera_con_mensaje(5)
    print("resultado")
    imprimir_matriz(sumamatriz)

if opc_1 == 2:
    print("usted encontrara A-B")
    print("Por lo tanto las matrices tienen que tener dimencsiones iguales (nxn)+(nxn)")
    filas_1 = int(input("Introduce el número de filas para la Matriz 1 (A): "))
    columnas_1 = int(input("Introduce el número de columnas para la Matriz 1 (A): "))
    filas_2 = int(input("Introduce el número de filas para la Matriz 2 (B): "))
    columnas_2 = int(input("Introduce el número de columnas para la Matriz 2 (B): "))
    while (filas_1!=filas_2)and(columnas_1!=columnas_2):
        print("Dimenciones distintas Pruebe denuevo ingresar los datos")
        print("usted encontrara A-B")
        print("Por lo tanto las matrices tienen que tener dimencsiones iguales")
        filas_1 = int(input("Introduce el número de filas para la Matriz 1 (A): "))
        columnas_1 = int(input("Introduce el número de columnas para la Matriz 1 (A): "))
        filas_2 = int(input("Introduce el número de filas para la Matriz 2 (B): "))
        columnas_2 = int(input("Introduce el número de columnas para la Matriz 2 (B): "))
    Matriz_1 = crear_matriz(filas_1,columnas_1)
    imprimir_matriz(Matriz_1)
    Matriz_2 = crear_matriz(filas_2,columnas_2)
    imprimir_matriz(Matriz_2)
    restamatriz = restar_matrices(Matriz_1,Matriz_2)
    espera_con_mensaje(5)
    print("resultado")
    imprimir_matriz(restamatriz)
if opc_1 == 3:
    print("usted encontrara A (mxn)*B (nxp)")
    print("Por lo tanto las matrices El número de columnas de la matriz A debe ser igual al número de filas de la matriz B)")
    filas_1 = int(input("Introduce el número de filas para la Matriz 1 (A): "))
    columnas_1 = int(input("Introduce el número de columnas para la Matriz 1 (A): "))
    filas_2 = int(input("Introduce el número de filas para la Matriz 2 (B): "))
    columnas_2 = int(input("Introduce el número de columnas para la Matriz 2 (B): "))
    while (columnas_1!=filas_2):
        print("Dimenciones incorrectas Pruebe denuevo ingresar los datos")
        print("usted encontrara A (mxn)*B (nxp)")
        print("Por lo tanto las matrices El número de columnas de la matriz A debe ser igual al número de filas de la matriz B)")
        filas_1 = int(input("Introduce el número de filas para la Matriz 1 (A): "))
        columnas_1 = int(input("Introduce el número de columnas para la Matriz 1 (A): "))
        filas_2 = int(input("Introduce el número de filas para la Matriz 2 (B): "))
        columnas_2 = int(input("Introduce el número de columnas para la Matriz 2 (B): "))
    Matriz_1 = crear_matriz(filas_1,columnas_1)
    imprimir_matriz(Matriz_1)
    Matriz_2 = crear_matriz(filas_2,columnas_2)
    imprimir_matriz(Matriz_2)
    Matriz_C=multiplicar_matrices(Matriz_1,Matriz_2)
    espera_con_mensaje(5)
    print("resultado")
    imprimir_matriz(Matriz_C)
if opc_1 == 4:
    print("usted encontrara k x A(mxn)")
    k = float(input("Ingrese una constante"))
    filas_1 = int(input("Introduce el número de filas para la Matriz 1 (A): "))
    columnas_1 = int(input("Introduce el número de columnas para la Matriz 1 (A): "))
    Matriz_1 = crear_matriz(filas_1,columnas_1)
    imprimir_matriz(Matriz_1)
    matriz_resultante = multiplicar_constante_matriz(k, Matriz_1)
    espera_con_mensaje(5)
    print("resultado")
    imprimir_matriz(matriz_resultante)

print("Creo que ya es suficiente")
