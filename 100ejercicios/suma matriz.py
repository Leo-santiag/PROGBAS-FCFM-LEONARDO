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
def crear_matriz():
    filas = int(input("Introduce el número de filas: "))
    columnas = int(input("Introduce el número de columnas: "))
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            valor = float(input(f"Introduce el valor para la posición ({i}, {j}): "))
            fila.append(valor)
        matriz.append(fila)
    return matriz
def imprimir_matriz(matriz):
    for fila in matriz:
        print(" ".join(map(str, fila)))

matriz1 = crear_matriz()  
matriz2 = crear_matriz()  
resultado = sumar_matrices(matriz1, matriz2)
print("Suma de las matrices:")
imprimir_matriz(resultado)
