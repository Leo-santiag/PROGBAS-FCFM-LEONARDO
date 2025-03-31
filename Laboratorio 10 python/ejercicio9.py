from matematicas import sumar

# Función estructurada
def ejemplo_procesamiento():
    numeros = list(range(1, 6))
    resultado = [sumar(n, 10) for n in numeros]  # Uso modular
    print("Lista procesada:", resultado)

# Clase para OOP
class Procesador:
    def __init__(self, datos):
        self.datos = datos

    def procesar_datos(self):
        return [dato * 2 for dato in self.datos]

# Ejecutar el programa completo
if __name__ == "__main__":
    ejemplo_procesamiento()

    # Paradigma Orientado a Objetos
    datos = [1, 2, 3, 4]
    procesador = Procesador(datos)
    print("Datos procesados:", procesador.procesar_datos())