import math
while True:
    try:
        a = float(input("Ingresa el valor del lado A del triangulo: "))
        b = float(input("Ingresa el valor del lado B del triangulo: "))
        c = float(input("Ingresa el valor del lado C del triangulo: "))
        break
    except ValueError:
        print("Error: Debes ingresar un número válido.")

def area(a, b, c):
    s = (a+b+c)/2
    return math.sqrt(s*(s-a)*(s-b)*(s-c))

def perimetro(a, b, c):
    return a+b+c

print(perimetro(a,b,c))
print(area(a,b,c))