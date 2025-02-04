print("Determinar si un número es par, impar o múltiplo de otro número")

numero = int(input("Introduzca un número: "))
multiplo_de = int(input("Introduzca otro número para verificar si el primero es múltiplo de él: "))

if numero % 2 == 0:
    print(f"{numero} es un número par.")
else:
    print(f"{numero} es un número impar.")

if numero % multiplo_de == 0:
    print(f"{numero} es múltiplo de {multiplo_de}.")
else:
    print(f"{numero} no es múltiplo de {multiplo_de}.")
