import random

# Función para generar una lista de números aleatorios
def generar_lista_aleatoria(tamaño, rango_min, rango_max):
    return [random.randint(rango_min, rango_max) for _ in range(tamaño)]

# Algoritmo de Quicksort
def quicksort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivote = lista[0]
        menores = [x for x in lista[1:] if x <= pivote]
        mayores = [x for x in lista[1:] if x > pivote]
        return quicksort(menores) + [pivote] + quicksort(mayores)

# Búsqueda binaria
def busqueda_binaria(lista, elemento):
    inicio= 0 
    fin = len(lista) - 1
    
    while inicio <= fin:
        #buscamos la pocicion de enmedio 
        medio = (inicio + fin) // 2
        #si el elemento que esta enmedio es igual al elemento busca regresa el elemento del medio 
        if lista[medio] == elemento:
            return medio
        #si el elemento que esta enmedio es menor al alemento buscado dividiremos la busqueda en dos partes y nos quedaremos con la lista de numero mayores a el elemento que se encuentra en el medio
        elif lista[medio] < elemento:
            #iniciamos en el elemento siguiente a el de enmedo 
            inicio = medio + 1
        #si no se cumple el de arriba tomaremos la parte que esta por debajo de el numero de enmedio
        else:
            #el inicio sera el mismo solo aue ahora el final es un elemento antes de el elemento central
            fin = medio - 1
    return -1

# Programa principal
tamaño = int(input("Introduce el tamaño de la lista: "))
rango_min = int(input("Introduce el valor mínimo: "))
rango_max = int(input("Introduce el valor máximo: "))

# Generar la lista de números aleatorios
lista = generar_lista_aleatoria(tamaño, rango_min, rango_max)
print(f"Lista generada: {lista}")

# Ordenar la lista usando Quicksort
lista_ordenada = quicksort(lista)
print(f"Lista ordenada: {lista_ordenada}")

# Buscar un número en la lista
numero_a_buscar = int(input("Introduce el número que quieres buscar: "))
posicion = busqueda_binaria(lista_ordenada, numero_a_buscar)

if posicion != -1:
    print(f"El número {numero_a_buscar} se encuentra en la posición {posicion} de la lista ordenada.")
else:
    print(f"El número {numero_a_buscar} no se encuentra en la lista.")