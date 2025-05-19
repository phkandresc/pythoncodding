'''
 Dise˜na un programa que calcule la media de cinco n´umeros depositados en las posiciones de memoria que van de la 10
 a la 14 y que deje el resultado en la direcci´on de memoria 15. Recuerda que la media ¯ x de cinco n´umeros x1, x2, x3, x4 y x5
 es
'''
numeros = range(10, 15)

def media(numeros):
    suma = 0
    for numero in numeros:
        suma += numero
    return suma / len(numeros)

print(media(numeros))# Imprime la media de los números en las posiciones de memoria 10 a 14

# Tambien existe la funcion mean() 