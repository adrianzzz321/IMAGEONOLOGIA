import imageio
import numpy as np

# Carga la imagen, la convierte a blanco y negro si es color, 
# asegura que esté en formato 0–255 y la devuelve lista para procesar.

def cargar_imagen(ruta):
    im = imageio.imread(ruta).astype(np.float32)
    if im.ndim == 3:
        im = np.mean(im, axis=2).astype(np.uint8)
    else:
        im = im.astype(np.uint8)
    print("Shape:", im.shape)
    print("Valor min:", im.min(), "max:", im.max(), "mean:", im.mean())
    return im

# 🧠 1. Cargar la imagen desde la ruta
# im = imageio.imread(ruta).astype(np.float32)


# imageio.imread lee cualquier imagen: JPG, PNG, TIF, etc.

# Razones para convertirla inmediatamente a float32:

# Facilita operaciones matemáticas posteriores.

# Evita overflow cuando se hacen filtros o multiplicaciones.

# Mantiene precisión sin usar demasiado espacio (como float64).

# En esta etapa, la imagen puede haber sido cargada como:

# uint8 si es normal (0–255)

# uint16 si es imagen médica/tif

# 3 canales si es color

# 1 canal si es blanco y negro

# 🧩 2. Detectar si la imagen es color (3 canales)
# if im.ndim == 3:


# im.ndim = número de dimensiones:

# 2 → Imagen en escala de grises (filas, columnas)

# 3 → Imagen RGB (filas, columnas, 3 canales)

# Entonces:

# ✔️ Si es una imagen RGB, hay que convertirla a escala de grises.
# ✔️ Si ya es una imagen gris, solo se estandariza el tipo de dato.

# 🎨 3. Convertir de RGB a escala de grises
# im = np.mean(im, axis=2).astype(np.uint8)


# Esto toma el promedio de:

# Rojo

# Verde

# Azul

# para obtener un valor único por píxel.

# El promedio es una forma rápida (aunque simple) de pasar de color a gris.
# Deja la imagen como una matriz 2D.

# Luego convierte a uint8 → valores de 0 a 255.

# ⚫ 4. Si ya era gris, solo normaliza el tipo
# else:
#     im = im.astype(np.uint8)


# Esto garantiza que:

# Todo el pipeline posterior trabaje con imágenes de 0–255.

# No haya imágenes flotantes raras, enteros grandes o valores negativos.

# Todos los filtros (median, gaussian, thresholding) reciban formatos consistentes.

# 🎁 5. Retornar
# return im


# Devuelve la imagen lista para ser procesada:

# En escala de grises

# En rango 0–255

# En formato uint8

# Con forma 2D (no 3 canales)