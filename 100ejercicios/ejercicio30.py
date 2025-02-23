def menu_principal():
    menu = """
    Bienvenido al Programa de Funciones Recursivas
    Elija una de las opciones:
    1. Calcular Factorial
    2. Calcular Secuencia de Fibonacci
    3. Sumar una Lista
    4. Salir
    """
    print(menu)
    return int(input("Seleccione una opción: "))

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_seq = fibonacci(n - 1)
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
        return fib_seq

def sumar_lista(lista):
    if len(lista) == 0:
        return 0
    else:
        return lista[0] + sumar_lista(lista[1:])

def main():
    while True:
        opcion = menu_principal()
        if opcion == 1:
            n = int(input("Ingrese un número para calcular su factorial: "))
            resultado = factorial(n)
            print(f"El factorial de {n} es {resultado}.")
        elif opcion == 2:
            n = int(input("Ingrese el número de términos de la secuencia de Fibonacci: "))
            resultado = fibonacci(n)
            print(f"Los primeros {n} términos de la secuencia de Fibonacci son: {resultado}.")
        elif opcion == 3:
            lista = input("Ingrese una lista de números separados por espacios: ")
            lista = list(map(int, lista.split()))
            resultado = sumar_lista(lista)
            print(f"La suma de la lista {lista} es {resultado}.")
        elif opcion == 4:
            print("Saliendo del programa de funciones recursivas. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")

if __name__ == "__main__":
    main()
