print("Verificar si un número es primo")
numero = int(input("Introduzca un número: "))

if numero > 1:
    for i in range(2, int(numero / 2) + 1):
        if (numero % i) == 0:
            print(f"{numero} no es un número primo.")
            break
    else:
        print(f"{numero} es un número primo.")
else:
    print(f"{numero} no es un número primo.")
