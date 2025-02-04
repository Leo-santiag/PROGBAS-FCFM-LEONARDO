print("Generar listas de números pares e impares hasta un límite dado")
limite = int(input("Introduzca el límite: "))
numeros_pares = [i for i in range(0, limite + 1) if i % 2 == 0]
numeros_impares = [i for i in range(0, limite + 1) if i % 2 != 0]
print(f"Números pares hasta {limite}: {numeros_pares}")
print(f"Números impares hasta {limite}: {numeros_impares}")
