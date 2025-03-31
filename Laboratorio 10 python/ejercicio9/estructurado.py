# Bloque estructurado
def es_par(numero):
    """Verifica si un número es par"""
    return numero % 2 == 0

def imprimir_pares(lista):
    """Imprime los números pares de una lista"""
    print("Números pares encontrados:")
    for num in lista:
        if es_par(num):  # Reutilizamos la función estructurada
            print(num)

# Ejemplo de uso
imprimir_pares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])