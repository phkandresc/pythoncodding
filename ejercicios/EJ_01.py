# 1 byte tiene 8 bits

# Convertir un número decimal a binario formato 8 bits
# Calcula las siguientes sumas de numeros codificados con 8 bits en el sistema posicional:

def decimal_a_binario(numero):
    if numero < 0 or numero > 255:
        raise ValueError("El número debe estar entre 0 y 255")
    
    binario = bin(numero)[2:]  # Convertir a binario y quitar el prefijo '0b' que significa binario
    binario = binario.zfill(8)  # Rellenar con ceros a la izquierda para que tenga 8 bits
    return binario

def suma_binarios(binario1, binario2):
    # Convertir los binarios a enteros, sumarlos y luego convertir el resultado de nuevo a binario
    suma_decimal = int(binario1, 2) + int(binario2, 2)
    return decimal_a_binario(suma_decimal)

print(decimal_a_binario(10))
print(suma_binarios("01111111", "00000001"))  # Suma de 127 y 1 en binario
