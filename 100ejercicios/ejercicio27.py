def menu_principal():
    menu = """
    Bienvenido al Conversor de Unidades
    Elija una de las opciones:
    1. Convertir Longitud
    2. Convertir Peso
    3. Convertir Temperatura
    4. Salir
    """
    print(menu)
    return int(input("Seleccione una opción: "))

def menu_longitud():
    menu = """
    Conversiones de Longitud:
    1. Metros a Kilómetros
    2. Kilómetros a Metros
    3. Metros a Millas
    4. Millas a Metros
    """
    print(menu)
    return int(input("Seleccione una opción: "))

def menu_peso():
    menu = """
    Conversiones de Peso:
    1. Kilogramos a Libras
    2. Libras a Kilogramos
    3. Gramos a Onzas
    4. Onzas a Gramos
    """
    print(menu)
    return int(input("Seleccione una opción: "))

def menu_temperatura():
    menu = """
    Conversiones de Temperatura:
    1. Celsius a Fahrenheit
    2. Fahrenheit a Celsius
    3. Celsius a Kelvin
    4. Kelvin a Celsius
    """
    print(menu)
    return int(input("Seleccione una opción: "))

def convertir_longitud(opcion):
    if opcion == 1:
        metros = float(input("Ingrese metros: "))
        print(f"{metros} metros son {metros / 1000} kilómetros.")
    elif opcion == 2:
        km = float(input("Ingrese kilómetros: "))
        print(f"{km} kilómetros son {km * 1000} metros.")
    elif opcion == 3:
        metros = float(input("Ingrese metros: "))
        print(f"{metros} metros son {metros * 0.000621371} millas.")
    elif opcion == 4:
        millas = float(input("Ingrese millas: "))
        print(f"{millas} millas son {millas / 0.000621371} metros.")

def convertir_peso(opcion):
    if opcion == 1:
        kg = float(input("Ingrese kilogramos: "))
        print(f"{kg} kilogramos son {kg * 2.20462} libras.")
    elif opcion == 2:
        libras = float(input("Ingrese libras: "))
        print(f"{libras} libras son {libras / 2.20462} kilogramos.")
    elif opcion == 3:
        gramos = float(input("Ingrese gramos: "))
        print(f"{gramos} gramos son {gramos / 28.3495} onzas.")
    elif opcion == 4:
        onzas = float(input("Ingrese onzas: "))
        print(f"{onzas} onzas son {onzas * 28.3495} gramos.")

def convertir_temperatura(opcion):
    if opcion == 1:
        celsius = float(input("Ingrese grados Celsius: "))
        print(f"{celsius} grados Celsius son {celsius * 9/5 + 32} grados Fahrenheit.")
    elif opcion == 2:
        fahrenheit = float(input("Ingrese grados Fahrenheit: "))
        print(f"{fahrenheit} grados Fahrenheit son {(fahrenheit - 32) * 5/9} grados Celsius.")
    elif opcion == 3:
        celsius = float(input("Ingrese grados Celsius: "))
        print(f"{celsius} grados Celsius son {celsius + 273.15} grados Kelvin.")
    elif opcion == 4:
        kelvin = float(input("Ingrese grados Kelvin: "))
        print(f"{kelvin} grados Kelvin son {kelvin - 273.15} grados Celsius.")

def main():
    while True:
        opcion_principal = menu_principal()
        if opcion_principal == 1:
            opcion_longitud = menu_longitud()
            convertir_longitud(opcion_longitud)
        elif opcion_principal == 2:
            opcion_peso = menu_peso()
            convertir_peso(opcion_peso)
        elif opcion_principal == 3:
            opcion_temperatura = menu_temperatura()
            convertir_temperatura(opcion_temperatura)
        elif opcion_principal == 4:
            print("Saliendo del conversor de unidades. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")

if __name__ == "__main__":
    main()
