while True:
    try:
        lado = float(input("Ingresa un número: "))
        break
    except ValueError:
        print("Error: Debes ingresar un número válido.")

print("Valor del perimetro =" + str(lado*4))
print("Valor del area =" + str(round(lado**2, 2)))