import math
while True:
    try:
        a = float(input("Ingresa una cantidad de euros: "))
        b = float(input("Ingresa una tasa de interes: "))
        c = float(input("Ingresa un numero de anios: "))
        break
    except ValueError:
        print("Error: Debes ingresar un número válido.")

def calcular_ganancia(capital, interes, anios):
    return capital * (1 + interes/100)**anios

print(calcular_ganancia(a, b, c))