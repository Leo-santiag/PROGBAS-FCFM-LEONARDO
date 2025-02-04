print("Calcula el factorial de un número dado")
numerodado = int(input("Introduzca un número dasdo: "))

if numerodado < 0:
    print("El factorial no está definido para números negativos.")
elif numerodado == 0:
    print("El factorial de 0 es 1.")
else:
    factorial = 1
    for i in range(1, numerodado + 1):
        factorial *= i
    print(f"El factorial de {numerodado} es {factorial}.")
