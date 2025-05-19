# Tablas de multiplicar

def mostrar_tabla(tabla):
    for i in range(1, 11):
        resultado = tabla * i
        print(f"{tabla} x {i} = {resultado}")

while True:
    try:
        tabla = int(input("¿Qué tabla de multiplicar quieres? "))
        mostrar_tabla(tabla)
    except ValueError:
        print("Por favor, introduce un número entero.")
        exit()

