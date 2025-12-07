from scipy.ndimage import median_filter, gaussian_filter
import numpy as np

# Esta función elimina ruido fuerte mediante un filtro de mediana y 
# luego suaviza la imagen con un filtro gaussiano, obteniendo un resultado limpio,
#  homogéneo y manteniendo los valores dentro de un rango válido.
def denoise_imagen(im_corr):
    im_med = median_filter(im_corr, size=3)
    im_gauss = gaussian_filter(im_med, sigma=1)
    im_denoise = np.clip(im_gauss, 0, 1).astype(np.float32)
    return im_denoise

# 🧠 1. ¿Qué objetivo tiene esta función?
# Eliminar ruido de la imagen sin perder demasiados detalles importantes.
# La función aplica dos filtros consecutivos:
# Mediana → elimina ruido en forma de puntos aislados (salt & pepper).
# Gaussiano → suaviza de manera uniforme, reduciendo ruido restante.
# Este combo se usa muchísimo en imágenes médicas, satelitales y visión computacional.
# 🧩 2. Filtro de Mediana
# im_med = median_filter(im_corr, size=3)
# ✔️ ¿Qué es?
# Es un filtro que reemplaza cada píxel por la mediana de sus vecinos.
# Para size=3, toma una ventana de 3×3 alrededor del píxel.
# ✔️ ¿Qué problema resuelve?
# Elimina muy bien el ruido impulsivo (puntos muy brillantes o muy oscuros).
# No difumina los bordes tanto como un filtro promedio o gaussiano.
# Ideal para imágenes donde aparecen “granitos” aislados.
# ✔️ Por qué se usa primero
# Si aplicaras el gaussiano primero, ese ruido impulsivo se “esparce” y se vuelve más difícil de quitar.
# Con la mediana, lo atacas desde el inicio sin afectar la estructura general.
# 🌫️ 3. Filtro Gaussiano
# im_gauss = gaussian_filter(im_med, sigma=1)
# ✔️ ¿Qué hace?
# Suaviza la imagen haciendo un promedio ponderado:
# Vecinos cercanos tienen más peso.
# Vecinos lejanos tienen menos peso.
# ✔️ ¿Por qué se aplica después?
# La mediana elimina ruido fuerte, pero puede dejar la imagen algo “áspera”.
# El gaussiano:
# Suaviza transiciones.
# Reduce ruido fino.
# Produce un acabado más limpio y natural.
# Un sigma=1 es suave, suficiente para limpiar sin borrar todos los detalles.
# ✂️ 4. Clip al rango [0,1]
# im_denoise = np.clip(im_gauss, 0, 1).astype(np.float32)
# Evita valores fuera del rango válido:
# Si algo queda < 0 → se vuelve 0
# Si algo queda > 1 → se vuelve 1
# ✔️ ¿Por qué es útil?
# Los filtros pueden producir valores negativos o mayores a 1 por las operaciones matemáticas.
# Clipping garantiza:
#Que la imagen se mantenga válida para visualización o modelos.
# Que no haya saturación inesperada.