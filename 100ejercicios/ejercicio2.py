print("calculadora simple")
try: 
    numero1= float(input("ingrese un numero"))
    operador = input("ingrese un simbolo como el siguiente \n(+)--suma\n(-)--resta\n(*)--multilicacion\n(/)--divicion\n")
    numero2= float(input("ingrese un numero"))

except:
 print("valor incorrecto")
operador=None
if operador==("+"):
 resultado=numero1+numero2
 print(resultado)
elif operador==("-"):
 resultado=numero1-numero2
 print(resultado)
elif operador==("*"):
 resultado=numero1*numero2
 print(resultado)
elif operador==("/"):
 resultado=numero1/numero2
 print(resultado)
else:
 print("dato incorrecto ingrese denuevo")