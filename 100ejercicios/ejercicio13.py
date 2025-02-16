print("Convertir una temperatura entre distintas escalas")
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_a_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_a_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_a_celsius(kelvin):
    return kelvin - 273.15

def kelvin_a_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def mostrar_menu():
    print("Selecciona la escala de temperatura inicial:")
    print("1. Celsius")
    print("2. Fahrenheit")
    print("3. Kelvin")

def convertir_temperatura(temp, escala_inicial, escala_final):
    if escala_inicial == 1:  
        if escala_final == 2:
            return celsius_a_fahrenheit(temp)
        elif escala_final == 3:
            return celsius_a_kelvin(temp)
    elif escala_inicial == 2:  
        if escala_final == 1:
            return fahrenheit_a_celsius(temp)
        elif escala_final == 3:
            return fahrenheit_a_kelvin(temp)
    elif escala_inicial == 3:  
        if escala_final == 1:
            return kelvin_a_celsius(temp)
        elif escala_final == 2:
            return kelvin_a_fahrenheit(temp)
    return temp  


mostrar_menu()
escala_inicial = int(input("Selecciona la escala inicial (1/2/3): "))

mostrar_menu()
escala_final = int(input("Selecciona la escala final (1/2/3): "))

temperatura = float(input("Ingresa la temperatura a convertir: "))

resultado = convertir_temperatura(temperatura, escala_inicial, escala_final)

escalas = {1: "Celsius", 2: "Fahrenheit", 3: "Kelvin"}
print(f"{temperatura} {escalas[escala_inicial]} son {resultado:.2f} {escalas[escala_final]}")

