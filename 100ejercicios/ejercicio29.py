import numpy as np
import matplotlib.pyplot as plt

def menu_principal():
    menu = """
    Bienvenido al Generador y Analizador de Datos Estadísticos
    Elija una de las opciones:
    1. Generar datos aleatorios
    2. Calcular estadísticas
    3. Mostrar histograma
    4. Mostrar gráfico de dispersión
    5. Salir
    """
    print(menu)
    return int(input("Seleccione una opción: "))

def generar_datos(cantidad, tipo='normal'):
    if tipo == 'normal':
        return np.random.randn(cantidad)
    elif tipo == 'uniforme':
        return np.random.rand(cantidad)
    else:
        print("Tipo de datos no soportado.")
        return np.array([])

def calcular_estadisticas(datos):
    print(f"Media: {np.mean(datos):.2f}")
    print(f"Mediana: {np.median(datos):.2f}")
    print(f"Desviación estándar: {np.std(datos):.2f}")
    print(f"Varianza: {np.var(datos):.2f}")

def mostrar_histograma(datos, bins=10):
    plt.hist(datos, bins=bins, edgecolor='black')
    plt.xlabel('Valores')
    plt.ylabel('Frecuencia')
    plt.title('Histograma')
    plt.show()

def mostrar_grafico_dispersion(datos):
    plt.scatter(range(len(datos)), datos, alpha=0.5)
    plt.xlabel('Índice')
    plt.ylabel('Valor')
    plt.title('Gráfico de Dispersión')
    plt.show()

def main():
    datos = np.array([])
    while True:
        opcion = menu_principal()
        if opcion == 1:
            cantidad = int(input("Ingrese la cantidad de datos a generar: "))
            tipo = input("Ingrese el tipo de datos a generar (normal/uniforme): ").strip().lower()
            datos = generar_datos(cantidad, tipo)
            print("Datos generados.")
        elif opcion == 2:
            if len(datos) == 0:
                print("Primero debe generar datos.")
            else:
                calcular_estadisticas(datos)
        elif opcion == 3:
            if len(datos) == 0:
                print("Primero debe generar datos.")
            else:
                bins = int(input("Ingrese el número de bins (intervalos) para el histograma: "))
                mostrar_histograma(datos, bins)
        elif opcion == 4:
            if len(datos) == 0:
                print("Primero debe generar datos.")
            else:
                mostrar_grafico_dispersion(datos)
        elif opcion == 5:
            print("Saliendo del generador y analizador de datos estadísticos. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")

if __name__ == "__main__":
    main()
