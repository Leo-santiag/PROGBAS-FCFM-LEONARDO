print("Encontrar el mayor de tres numeros")
lista = list()
i = 0
for i in range(1,4):
    lista += input(f"ingrese el numero {i}")
    i +=1
i = 0
mayor = lista[1]
for i in lista:
    if mayor <= i:
        mayor =i
        
print(f"El numero mayor es {mayor} ")