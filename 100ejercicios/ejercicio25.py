import numpy as np
import matplotlib.pyplot as plt

def menu_principal():
    menu = """
    Bienvenido al Generador y Analizador de Histogramas
    Elija una de las opciones:
    1. Generar histograma de datos aleatorios
    2. Analizar histograma
    3. Salir
    """
    print(menu)
    return int(input("Seleccione una opción: "))

def generar_histograma(datos, bins=10):
    plt.hist(datos, bins=bins, edgecolor='black')
    plt.xlabel('Valores')
    plt.ylabel('Frecuencia')
    plt.title('Histograma')
    plt.show()

def analizar_histograma(datos):
    print(f"Media: {np.mean(datos):.2f}")
    print(f"Mediana: {np.median(datos):.2f}")
    print(f"Desviación estándar: {np.std(datos):.2f}")
    print(f"Varianza: {np.var(datos):.2f}")

def main():
    datos = []
    while True:
        opcion = menu_principal()
        if opcion == 1:
            cantidad_datos = int(input("Ingrese la cantidad de datos a generar: "))
            datos = np.random.randn(cantidad_datos)
            bins = int(input("Ingrese el número de bins (intervalos) para el histograma: "))
            generar_histograma(datos, bins)
        elif opcion == 2:
            if len(datos) == 0:
                print("Primero debe generar un histograma de datos aleatorios.")
            else:
                analizar_histograma(datos)
        elif opcion == 3:
            print("Saliendo del generador y analizador de histogramas. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")

if __name__ == "__main__":
    main()
