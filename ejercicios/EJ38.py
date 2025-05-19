import math
while True:
    try:
        a = float(input("Ingresa el valor del lado A del triangulo: "))
        b = float(input("Ingresa el valor del lado B del triangulo: "))
        angulo = float(input("Ingresa el valor del angulo entre A y B: "))
        break
    except ValueError:
        print("Error: Debes ingresar un número válido.")

def area(a, b, angulo):
    return 0.5 * a * b * math.sin(math.radians(angulo))

print(area(a,b,angulo))

