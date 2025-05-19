while True:
    try:
        b = float(input("Ingresa el valor de la base del rectangulo: "))
        a = float(input("Ingresa el valor de la altura del rectangulo: "))
        break
    except ValueError:
        print("Error: Debes ingresar un número válido.")

perimetro = b*2 + a*2
area = b*a/2

print(f"El perimetro es {perimetro}")
print(f"El area es {area}")