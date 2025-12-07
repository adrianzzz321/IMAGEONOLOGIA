import numpy as np
from skimage.measure import regionprops


# La función recorre todos los núcleos segmentados, mide qué tan grandes son 
# y qué tan brillantes son, imprime unos datos básicos 
# (cuántos hay, área mínima, máxima y promedio)
#  y te devuelve toda esa información lista para analizar.

def analizar_nucleos(labels_ws, sharpened_im):
    props = regionprops(labels_ws, intensity_image=sharpened_im)

    areas = []
    intensidades = []

    for r in props:
        areas.append(r.area)
        intensidades.append(r.mean_intensity)

    areas = np.array(areas)
    intensidades = np.array(intensidades)

    print("Número de núcleos detectados:", len(props))
    print("Área mínima:", np.min(areas))
    print("Área máxima:", np.max(areas))
    print("Área promedio:", np.mean(areas))

    return props, areas, intensidades

# 🧠 1. ¿Qué son labels_ws y sharpened_im?

# labels_ws: es la imagen segmentada por watershed.

# Es una imagen donde:

# 0 = fondo

# 1, 2, 3, ... = cada núcleo como un objeto distinto.

# sharpened_im: es la imagen realzada (más nítida) que usas como intensity_image para medir intensidad dentro de cada núcleo.

# La idea es:

# “Tengo una etiqueta para cada núcleo y una imagen con las intensidades, ahora quiero medir cosas de cada núcleo”.

# 🧩 2. regionprops: obtener propiedades de cada núcleo
# props = regionprops(labels_ws, intensity_image=sharpened_im)


# regionprops analiza todos los objetos conectados en labels_ws y te da una lista de objetos (uno por núcleo), donde cada objeto r tiene muchas propiedades ya calculadas, por ejemplo:

# r.area → cantidad de píxeles del núcleo.

# r.mean_intensity → intensidad media dentro del núcleo.

# r.centroid → centroide.

# r.perimeter, r.eccentricity, etc. (si los quisieras usar).

# Aquí estamos usando dos: area e intensidad media.

# 📥 3. Recorrer cada núcleo y guardar área e intensidad
# areas = []
# intensidades = []

# for r in props:
#     areas.append(r.area)
#     intensidades.append(r.mean_intensity)


# Para cada núcleo r:

# r.area: qué tan grande es el núcleo en píxeles.

# r.mean_intensity: qué tan brillante es, en promedio.

# Se van guardando en dos listas paralelas:

# areas[i] → área del núcleo i

# intensidades[i] → intensidad media del mismo núcleo i

# Esto te deja los datos listos para análisis cuantitativo.

# 🔁 4. Convertir a arreglos de NumPy
# areas = np.array(areas)
# intensidades = np.array(intensidades)


# Convertir listas a numpy.array te permite:

# Calcular mínimos, máximos, promedios, percentiles, etc.

# Usar operaciones vectorizadas (más rápido y más cómodo).

# 📊 5. Imprimir estadísticas básicas
# print("Número de núcleos detectados:", len(props))
# print("Área mínima:", np.min(areas))
# print("Área máxima:", np.max(areas))
# print("Área promedio:", np.mean(areas))


# Lo que muestra:

# Número de núcleos detectados → cuántos objetos encontró el watershed.

# Área mínima → el núcleo más pequeño.

# Área máxima → el núcleo más grande.

# Área promedio → tamaño promedio de un núcleo.

# Estas estadísticas te dan una idea rápida de:

# ¿La segmentación tiene sentido?

# ¿Hay núcleos muy pequeños (ruido)?

# ¿Hay núcleos gigantes (posibles fusiones)?

# 🎁 6. Lo que devuelve la función
# return props, areas, intensidades


# Te devuelve:

# props: la lista completa de regiones (regionprops) para acceder a cualquier propiedad avanzada (centroides, perímetros, etc.).

# areas: vector con las áreas de todos los núcleos.

# intensidades: vector con las intensidades medias.

# Luego usas esto para:

# Hacer histogramas.

# Detectar núcleos sospechosos.

# Hacer análisis estadístico, tablas, etc.