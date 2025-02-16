print("Saber si una palabra es un palíndromo")
palabra = input("Ingrese una palabra para iniciar la verificación: ")
Tamaño = len(palabra)
print(Tamaño)
i = 0
z = -1
es_palindromo = True

while (Tamaño / 2) > i:
    print("llega hasta aqui")
    if palabra[i] != palabra[z]:
        es_palindromo = False
        break
    
    print(palabra[i])
    print(palabra[z])
    i += 1
    z -= 1

if es_palindromo:
    print("es un palíndromo")
else:
    print("no es un palíndromo")
