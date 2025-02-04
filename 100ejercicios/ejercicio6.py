print("Calcular el interés compuesto dado un capital, tasa y tiempo")

capital = float(input("Introduzca el capital inicial: "))
tasa = float(input("Introduzca la tasa de interés anual (en %): ")) / 100
tiempo = float(input("Introduzca el tiempo en años: "))
compounded_per_year = int(input("Introduzca el número de veces que se aplica el interés por año: "))

monto_final = capital * (1 + tasa / compounded_per_year) ** (compounded_per_year * tiempo)
interes_compuesto = monto_final - capital

print(f"El monto final después de {tiempo} años es: {monto_final:.2f}")
print(f"El interés compuesto es: {interes_compuesto:.2f}")
