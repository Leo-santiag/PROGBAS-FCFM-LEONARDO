import cmath

print("Resolver ecuaciones cuadráticas.\nVerifique que la ecuación esté igualada a 0")

a = float(input("Ingrese el coeficiente del término cuadrático (a): "))
b = float(input("Ingrese el coeficiente del término lineal (b): "))
c = float(input("Ingrese el coeficiente del término independiente (c): "))

discriminante = (b**2) - (4*a*c)
print(f"El discriminante es igual a {discriminante}")

if discriminante < 0:
    print("Solución imaginaria")
    discriminante *= -1
    x1 = (-b)/ (2*a) 
    x11 = (discriminante**0.5) / (2*a)
    x2 = (-b)/ (2*a) 
    x22 = (discriminante**0.5) / (2*a)
    print(f"La solución 1 es igual a {x1}+{x11}i, la solución 2 es igual a {x2}+{x22}i")
elif discriminante == 0:
    x = -b / (2*a)
    print(f"La solución es única y es igual a {x}")
else:
    x1 = (-b + discriminante**0.5) / (2*a)
    x2 = (-b - discriminante**0.5) / (2*a)
    print(f"La solución 1 es igual a {x1}, la solución 2 es igual a {x2}")
