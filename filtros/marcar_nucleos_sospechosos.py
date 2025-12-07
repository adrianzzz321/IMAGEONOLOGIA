import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Dibuja un círculo amarillo alrededor de cada núcleo sospechoso usando su centro 
# y tamaño para ayudarte a visualizarlos claramente en la imagen.

def marcar_nucleos_sospechosos(im, nucleos_sospechosos,
                               radio_max=30):
    plt.figure(figsize=(6,6))
    plt.imshow(im, cmap="gray")
    ax = plt.gca()

    for r in nucleos_sospechosos:
        cy, cx = r.centroid     # centro (fila, columna)
        radius = r.equivalent_diameter / 2.0

        # Limitar el radio para que no haya círculos gigantes
        radius = min(radius, radio_max)

        circ = patches.Circle((cx, cy), radius,
                              edgecolor='yellow',
                              facecolor='none',
                              linewidth=2)
        ax.add_patch(circ)

    plt.title("Núcleos Sospechosos Marcados")
    plt.axis("off")
    plt.show()

# 🧠 1. Crear la figura y mostrar la imagen
# plt.figure(figsize=(6,6))
# plt.imshow(im, cmap="gray")
# ax = plt.gca()

# ¿Qué hace esto?

# Crea una figura cuadrada de 6×6 pulgadas.

# Muestra la imagen im (generalmente la imagen realzada o la original).

# Obtiene el objeto axes (ax) que representa el área donde se plotea la imagen.

# ax será necesario para agregar los círculos encima de la imagen.

# 🧩 2. Recorrer la lista de núcleos sospechosos
# for r in nucleos_sospechosos:


# Cada elemento de esta lista es un objeto de regionprops, que contiene información geométrica y de intensidad del núcleo.

# 🎯 3. Obtener centro y radio del núcleo
# cy, cx = r.centroid
# radius = r.equivalent_diameter / 2.0

# Explicación:

# r.centroid → devuelve la posición del centro del núcleo como (fila, columna)

# En coordenadas de la imagen:

# cy = y (fila)

# cx = x (columna)

# r.equivalent_diameter → es el diámetro del círculo que tendría la misma área que el núcleo.

# Entonces:

# radio = diámetro_equivalente / 2


# Esto te da un círculo aproximado que rodea al núcleo.

# 🟡 4. Dibujar un círculo amarillo
# circ = patches.Circle((cx, cy), radius, 
#                       edgecolor='yellow', 
#                       facecolor='none', 
#                       linewidth=2)
# ax.add_patch(circ)

# ¿Qué hace esto?

# Crea un círculo con centro (cx, cy) y radio radius.

# Solo dibuja el borde (facecolor='none') para no tapar la imagen.

# Línea amarilla y gruesa (linewidth=2) para que destaque.

# ax.add_patch() lo coloca encima de la imagen.

# Así cada núcleo sospechoso queda visualmente marcado.

# 🖼️ 5. Finalizar la visualización
# plt.title("Núcleos Sospechosos Marcados")
# plt.axis("off")
# plt.show()


# Esto:

# Quita los ejes de la imagen.

# Coloca un título descriptivo.

# Muestra la imagen final.