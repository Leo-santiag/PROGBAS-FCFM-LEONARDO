import random

def lanzar_moneda():
    resultado = random.choice(['Cara', 'Cruz'])
    return resultado


for _ in range(10):  
    print(lanzar_moneda())
