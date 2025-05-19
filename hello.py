# commentary

print("Hello, World!")

"""
This is a simple Python script that prints "Hello, World!" to the console.
It serves as a basic introduction to Python programming and demonstrates the use of the print function.
"""

print(type("Hello, World!"))
print(type(1))
print(type(1.0))
print(type(True))
print(type(None))
print(type([]))
print(type({}))
print(type(()))

print(sum([1, 2, 3]))
print(1,2,3)

#Dinamicamente tipado
x = 10
x = "ahora soy un string"

#inicializar multiples variables
a, b, c = 1, 2, 3

#Asignar el mismo valor a varias variables
x = y = z = 0

from enum import Enum

class EstadoTarea(Enum):
    PENDIENTE = 1
    EN_PROGRESO = 2
    COMPLETADA = 3

numeros = [1, 2, 3, 4, 5]

for numero in numeros:
    print(numero)

#metodos de listas
numeros.append(6) # Agregar un elemento al final de la lista
numeros.insert(0, 0) # Insertar un elemento en una posición específica
numeros.remove(3) # Eliminar un elemento específico
numeros.pop() # Eliminar el último elemento de la lista
numeros.sort() # Ordenar la lista en orden ascendente
numeros.reverse() # Invertir el orden de la lista
numeros.clear() # Limpiar todos los elementos de la lista

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matriz[1][2])  # Resultado: 6

persona = {
    "nombre": "Ana",
    "edad": 28,
    "ciudad": "Bogotá"
}

#🔎 Acceder a valores:
print(persona["nombre"])  # Ana

#✏️ Modificar valores:
persona["edad"] = 29

#➕ Agregar un nuevo par:
persona["profesion"] = "Ingeniera"

#❌ Eliminar un par:
del persona["ciudad"]

#🔁 Recorrer un diccionario:
for clave, valor in persona.items():
    print(clave, "→", valor)

class Persona:
    def __init__(self, nombre, edad, ciudad):
        self.nombre = nombre
        self.edad = edad
        self.ciudad = ciudad

p = Persona("Ana", 28, "Bogotá")
print(p.nombre)  # Ana

#Operadores relacionales
# ==, !=, >, <, >=, <=
print(1 == 1)  # True
print(1 != 2)  # True
print(1 > 2)   # False
print(1 < 2)   # True
print(1 >= 1)  # True
print(1 <= 2)  # True
# and, or, not
print(True and False)  # False
print(True or False)   # True
print(not True)        # False


usuario = None

# Sin cortocircuito (esto fallaría)
# if usuario != None and usuario["nombre"] == "Ana":

# Con cortocircuito (forma correcta)
if usuario and usuario["nombre"] == "Ana":
    print("Hola Ana")
else:
    print("Usuario inválido")


nota = 75

if nota >= 90:
    print("Excelente")
elif nota >= 60:
    print("Aprobado")
else:
    print("Reprobado")

def agregar(lista):
    lista.append(4)

datos = [1, 2, 3]
agregar(datos)
print(datos)  # ➝ [1, 2, 3, 4]

mi_tupla = (1, "hola", 3.5)

t = (10, 20, 30)
print(t[0])  # 10
print(t[-1]) # 30 (último)
