from conversor import kilometros_a_millas, celsius_a_fahrenheit, litros_a_galones

def mostrar_menu():
    print("\nMenú de opciones:")
    print("1. convertir kilómetros a millas")
    print("2. convertir celsius a fahrenheit")
    print("3. convertir litros a galones")
    print("4. salir")

while True:
    mostrar_menu()
    opcion = input("Elige una opción (1-4): ")

    if opcion == "1":
        km = float(input("introduce la cantidad de kilómetros: "))
        print(f"{km} kilómetros son {kilometros_a_millas(km):.2f} millas.")

    elif opcion == "2":
        celsius = float(input("Introduce la temperatura en grados Celsius: "))
        print(f"{celsius}° celsius son {celsius_a_fahrenheit(celsius):.2f}° fahrenheit.")

    elif opcion == "3":
        litros = float(input("Introduce la cantidad de litros: "))
        print(f"{litros} litros son {litros_a_galones(litros):.2f} galones.")

    elif opcion == "4":
        print("adios")
        break

    else:
        print("opción inválida. por favor, elige una opción del 1 al 4.")