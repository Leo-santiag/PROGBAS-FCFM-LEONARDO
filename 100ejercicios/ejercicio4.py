print("Generar la secuencia de Fibonacci para un número dado de términos ")
numerodadodeterminos = int(input("Introduzca un número dado de términos: "))

if numerodadodeterminos <= 0:
    print("Número incorrecto.")
elif numerodadodeterminos == 1:
    print(0)
else:
    fibonacci = [0, 1]
    print(fibonacci[0])
    print(fibonacci[1])
    for i in range(2, numerodadodeterminos):
        siguiente = fibonacci[i - 1] + fibonacci[i - 2]
        fibonacci.append(siguiente)
        print(siguiente)
