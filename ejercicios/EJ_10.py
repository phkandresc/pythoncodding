'''
Dise˜na un algoritmo que calcule el IVA (16%) de un producto dado su precio de venta sin IVA.
'''

def agregar_iva(precio_sin_iva):
    iva = 0.16 * precio_sin_iva
    precio_con_iva = precio_sin_iva + iva
    return precio_con_iva, iva

print(agregar_iva(100))  # Imprime el precio con IVA y el IVA correspondiente

print(True==True!=False)
print(1<2<3<4<5)
print((1<2<3)and(4<5))
print(1<2<4<3<5)
print((1<2<4)and(3<5))

print('123'< '13') # True

