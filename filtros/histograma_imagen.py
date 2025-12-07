
import scipy.ndimage as ndi

# Cuenta cuántos píxeles tiene cada valor de 0 a 255 y devuelve esa lista como el histograma de la imagen.

def histograma_imagen(img_u8):
    hist = ndi.histogram(img_u8, min=0, max=256, bins=256)
    return hist

# 🧠 1. ¿Qué es un histograma de imagen?

# Un histograma en procesamiento de imágenes cuenta cuántos píxeles tienen cada nivel de intensidad.

# Para una imagen de 8 bits (0–255):

# El histograma tendrá 256 barras.

# Cada barra indica cuántos píxeles tienen ese valor exacto.

# Ejemplo:
# hist[120] = 5000 → hay 5000 píxeles de intensidad 120.

# El histograma se usa para:

# Ecualización de la imagen

# Detección de umbrales

# Análisis de contraste

# Detección de patrones en microscopía

# 🧩 2. Uso de ndi.histogram
# hist = ndi.histogram(img_u8, min=0, max=256, bins=256)


# Esta función devuelve un arreglo de tamaño 256, uno por cada bin:

# bins=256 → un bin por cada intensidad (0 a 255).

# min=0 y max=256 → rango completo de intensidades posibles.

# ndi.histogram() es muy rápido y eficiente, especialmente con imágenes grandes, porque está optimizado en C.

# 📌 ¿Qué hace exactamente?

# Cuenta los píxeles que caen dentro de cada rango.
# Como es una imagen de 0–255, cada rango (bin) es exactamente un valor entero.

# El resultado es algo así como:

# [1023, 800, 1200, ..., 50]


# donde:

# hist[0] → número de píxeles con valor 0

# hist[1] → número de píxeles con valor 1

# …

# hist[255] → número de píxeles con valor 255

# 🎁 3. Lo que devuelve la función
# return hist


# Devuelve un vector de frecuencias:

# Longitud: 256

# Tipo: enteros

# Representa la distribución de intensidades de la imagen

# Este histograma lo usas luego para construir la CDF, que a su vez sirve para la ecualización.