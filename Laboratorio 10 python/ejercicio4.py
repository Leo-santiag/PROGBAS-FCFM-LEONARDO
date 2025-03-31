import math

def calculadora_estadisticas(*args):
    # Convertir los argumentos en una lista
    numeros = list(args)
    # Promedio usando una función lambda
    promedio = (lambda lista: sum(lista) / len(lista) if lista else 0)(numeros)
    # Mediana
    #sorted es un metodo que devuelve una cadena ordenada de mayor a menor la cadena original no se altera, se puede añadir reverse = True para cambiarl al a menor a mayor
    numeros_ordenados = sorted(numeros)
    n = len(numeros_ordenados)
    mediana = (lambda lista: lista[n // 2] if n % 2 != 0 else (lista[n // 2 - 1] + lista[n // 2]) / 2)(numeros_ordenados)

    # Desviación estándar
    desviacion_estandar = math.sqrt(sum((x - promedio) ** 2 for x in numeros) / n) if n > 0 else 0

    return promedio, mediana, desviacion_estandar

# Solicitar al usuario una lista de números
entrada = input("Introduce una lista de números separados por comas: ")
#el metodo split separa elemento de una caden por el argumento que le pases
lista_numeros = [float(num) for num in entrada.split(",")]

# Calcular y mostrar los resultados
promedio, mediana, desviacion_estandar = calculadora_estadisticas(*lista_numeros)
print(f"\nResultados:")
print(f"Promedio: {promedio:.2f}")
print(f"Mediana: {mediana:.2f}")
print(f"Desviación Estándar: {desviacion_estandar:.2f}")