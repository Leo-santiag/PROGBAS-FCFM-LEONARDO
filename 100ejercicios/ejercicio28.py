class CuentaBancaria:
    def __init__(self, nombre):
        self.nombre = nombre
        self.saldo = 0

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Se han depositado ${cantidad:.2f}. Saldo actual: ${self.saldo:.2f}.")
        else:
            print("La cantidad a depositar debe ser mayor que cero.")

    def retirar(self, cantidad):
        if 0 < cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"Se han retirado ${cantidad:.2f}. Saldo actual: ${self.saldo:.2f}.")
        else:
            print("La cantidad a retirar es inválida o excede el saldo disponible.")

    def ver_saldo(self):
        print(f"Saldo actual: ${self.saldo:.2f}")

def menu_principal():
    menu = """
    Bienvenido al Simulador de Cuenta Bancaria
    Elija una de las opciones:
    1. Depositar
    2. Retirar
    3. Ver Saldo
    4. Salir
    """
    print(menu)
    return int(input("Seleccione una opción: "))

def main():
    nombre = input("Ingrese su nombre: ")
    cuenta = CuentaBancaria(nombre)
    while True:
        opcion = menu_principal()
        if opcion == 1:
            cantidad = float(input("Ingrese la cantidad a depositar: "))
            cuenta.depositar(cantidad)
        elif opcion == 2:
            cantidad = float(input("Ingrese la cantidad a retirar: "))
            cuenta.retirar(cantidad)
        elif opcion == 3:
            cuenta.ver_saldo()
        elif opcion == 4:
            print("Saliendo del simulador de cuenta bancaria. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")

if __name__ == "__main__":
    main()
