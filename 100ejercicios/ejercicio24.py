def suma_serie_aritmetica(a1, an, n):
    return (n / 2) * (a1 + an)
def suma_serie_geometrica(a, r, n):
    if r == 1:
        return a * n
    return a * (1 - r ** n) / (1 - r)
def menu():
    menu=""""
    INICIO
    SERIES
    Elija un tipo se serie
    >>>>(1)Aritmetica
    >>>>(2)Geometrica
    >>>>
    """
    print(menu)
    return int(input())
eleccion=menu()
if eleccion ==1:
    a1=float(input("ingrese el primer termino"))
    an=float(input("ingrese el ultimo termino"))
    n =float(input("ingrese el numero de terminos"))
    resultado = suma_serie_aritmetica(a1, an, n)
    print(resultado)
if eleccion ==2:
    a=float(input("ingrese el primer termino"))
    r=float(input("ingrese la razon"))
    n =float(input("ingrese el numero de terminos"))
    resultado = suma_serie_geometrica(a, r, n)
    print(resultado)