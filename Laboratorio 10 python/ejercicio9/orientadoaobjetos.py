# Bloque orientado a objetos
class Vehiculo:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def mostrar_informacion(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.año}"

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, año, puertas):
        super().__init__(marca, modelo, año)
        self.puertas = puertas

    def mostrar_informacion(self):
        info_base = super().mostrar_informacion()
        return f"{info_base}, Puertas: {self.puertas}"

# crear objeto y mostrar información
mi_auto = Automovil("Toyota", "Corolla", 2020, 4)
print(mi_auto.mostrar_informacion())