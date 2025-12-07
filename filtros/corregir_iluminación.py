import numpy as np
from scipy.ndimage import gaussian_filter

# Suaviza muchísimo la imagen para estimar la iluminación del fondo y 
# luego divide la imagen original por ese fondo para corregir 
# zonas demasiado oscuras o brillantes, dejando la iluminación pareja en
#  toda la imagen.

def corregir_iluminacion(im_norm, sigma=60):
   
    fondo = gaussian_filter(im_norm, sigma=sigma)
    corr = im_norm / (fondo + 1e-8)
    return np.clip(corr, 0, 1)

# 🧠 1. ¿Qué problema resuelve esta función?

# Las imágenes microscópicas suelen tener variaciones de iluminación:

# Zonas más brillantes o más oscuras.

# Iluminación no uniforme del microscopio.

# Manchas o sombras del sensor.

# Eso provoca que la segmentación y el contraste salgan mal si no se corrige antes.

# Esta función aplica una técnica llamada "background correction" o corrección de campo iluminado".

# 🧩 2. Estimar el fondo usando un filtro gaussiano muy grande
# fondo = gaussian_filter(im_norm, sigma=sigma)


# Aquí ocurre algo clave:

# Un filtro gaussiano con sigma muy grande (60) genera una versión extremadamente suave de la imagen.

# Esa versión suave contiene solo la iluminación global, no los detalles.

# La idea es:

# 👉 Un Gaussian enorme elimina estructuras pequeñas (células, núcleos)
# 👉 Mantiene solo la variación de iluminación

# Ese resultado es una estimación del fondo ("background").

# Ejemplo mental:
# Es como si difuminaras una foto hasta que solo quedaran manchas de luz, sin detalles.

# ⚡ 3. Corregir la imagen dividiéndola por el fondo
# corr = im_norm / (fondo + 1e-8)


# ¿Por qué dividir?

# Porque:

# Si una zona está muy iluminada, el fondo es grande → al dividir ↓ la intensidad baja.

# Si una zona está oscura, el fondo es pequeño → al dividir ↑ la intensidad sube.

# Esto iguala la iluminación en toda la imagen.

# El 1e-8 evita dividir por cero.

# ¿Qué efecto produce?

# ✔️ La imagen queda mucho más uniforme.
# ✔️ Las células se ven con un brillo homogéneo.
# ✔️ La segmentación posterior funciona mejor.

# 🎚️ 4. Limitar valores al rango 0–1
# return np.clip(corr, 0, 1)


# Después de dividir:

# Algunos valores podrían quedar > 1

# Otros podrían quedar negativos (poco probable pero posible)

# np.clip recorta todo:

# Valores < 0 → se vuelven 0

# Valores > 1 → se vuelven 1

# Esto deja la imagen lista para usar.