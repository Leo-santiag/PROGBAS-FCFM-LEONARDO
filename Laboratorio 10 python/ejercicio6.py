'''1.3 Clases
 Ejercicio 6: Sistema de Gestion de Vehıculos
 Crea una clase Vehiculo con los siguientes atributos y m etodos:

 Atributos: marca, modelo, a no y precio.
 
 
 Metodo para mostrar la informacion del vehıculo.
 Crear subclases Automovil y Motocicleta con atributos adicionales como
 numero de puertas o cilindrada.'''

class Vehiculo():
    def __init__(self,marca,modelo,año,precio):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.precio = precio
    def mostrar_informacion_del_vehiculo(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.año}, Precio: ${self.precio:.2f}"
        

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, año, precio,numerodepuertas):
        super().__init__(marca, modelo, año, precio)
        self.numerodepuertas = numerodepuertas
    def mostrar_informacion_del_vehiculo(self):
        return f"{super().mostrar_informacion_del_vehiculo()}, Numero de puertas: {self.numerodepuertas}"
class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, año, precio,cilindrada):
        super().__init__(marca, modelo, año, precio)
        self.cilindrada = cilindrada
    def mostrar_informacion_del_vehiculo(self):
        return f"{super().mostrar_informacion_del_vehiculo()}, Cilindrada: {self.cilindrada}cc"
    
auto = Automovil("Toyota", "Corolla", 2020, 20000, 4)
moto = Motocicleta("Yamaha", "MT-03", 2021, 5500, 321)

print(auto.mostrar_informacion_del_vehiculo())
print(moto.mostrar_informacion_del_vehiculo())
