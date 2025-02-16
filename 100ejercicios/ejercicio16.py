print("Contar el numero de vocales y consonantes en una cadena ")
cadena = input("ingrese una cadena de caracteres\n")
print(cadena)
cadenasinespacios= cadena.replace(" ","")
print(cadenasinespacios)
cadenaminusculas = cadenasinespacios.lower()
print(cadenaminusculas)
caracteres = len(cadenasinespacios)
vocales = ['a', 'e', 'i', 'o', 'u']

i=1
contvocales = 0
while caracteres > i:
    for vocal in vocales:
        if cadenaminusculas[i] == vocal:
            contvocales += 1
    i+=1
consonantes = caracteres - contvocales
print(f"El numero de vocales es {contvocales} y el numero de consonantes es {consonantes}")