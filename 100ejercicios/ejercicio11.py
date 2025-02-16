print("definir si una palabra es palindromo")
palabra= input("ingresa una palabra")

palabrainvertida = ""
cont = len(palabra)
while cont > 0:
    
    palabrainvertida += palabra[cont - 1]
    print(palabrainvertida)
    
    cont = cont - 1
if palabra == palabrainvertida:
    print(" es un palindromo")
else:
    print("no es un palindromo")