import math
print("Calcular el área y la circunferencia de un círculo")
radio = float(input("Introduzca el radio del círculo: "))
area = math.pi * radio ** 2
circunferencia = 2 * math.pi * radio
print(f"El área del círculo es: {area:.2f}")
print(f"La circunferencia del círculo es: {circunferencia:.2f}")
