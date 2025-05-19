import matplotlib.pyplot as plt

# Coordenadas de las esquinas
x1, y1 = 100, 100  # Inferior izquierda
x2, y2 = 900, 900  # Superior derecha

# Crear figura y ejes
fig, ax = plt.subplots()

# Dibujar el cuadrado
square_x = [x1, x2, x2, x1, x1]
square_y = [y1, y1, y2, y2, y1]
ax.plot(square_x, square_y, 'k')  # 'k' es negro

# Dibujar las diagonales
ax.plot([x1, x2], [y1, y2], 'k')  # Diagonal de (100,100) a (900,900)
ax.plot([x1, x2], [y2, y1], 'k')  # Diagonal de (100,900) a (900,100)

# Configurar límites y aspecto
ax.set_xlim(0, 1000)
ax.set_ylim(0, 1000)
ax.set_aspect('equal')

# Mostrar coordenadas como texto
ax.text(x1, y1 - 30, f'({x1}, {y1})', ha='center')
ax.text(x2, y2 + 20, f'({x2}, {y2})', ha='center')

plt.axis('off')  # Opcional: oculta los ejes
plt.show()
