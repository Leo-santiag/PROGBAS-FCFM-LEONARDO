def busqueda_lineal(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i  
    return -1  


arr = [2, 4, 6, 8, 10]
x = 6
resultado = busqueda_lineal(arr, x)
print(f"Elemento encontrado en el índice: {resultado}" if resultado != -1 else "Elemento no encontrado")

def busqueda_binaria(arr, x):
    izquierda = 0
    derecha = len(arr) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if arr[medio] == x:
            return medio  
        elif arr[medio] < x:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return -1  


arr = [2, 4, 6, 8, 10]
x = 6
resultado = busqueda_binaria(arr, x)
print(f"Elemento encontrado en el índice: {resultado}" if resultado != -1 else "Elemento no encontrado")
