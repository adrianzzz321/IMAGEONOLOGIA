import numpy as np
from scipy.ndimage import gaussian_filter
# Realce de bordes y detalles
# La función:
# Hace un desenfoque suave y uno más fuerte, los resta para obtener detalles 
# y bordes, y luego suma esos detalles a la imagen original para que se vea más nítida,
# asegurándose de que los valores sigan entre 0 y 1.
def realzar_imagen(im_eq):

    blur1 = gaussian_filter(im_eq, sigma=1)
    blur2 = gaussian_filter(im_eq, sigma=2)
    dog = blur1 - blur2   
    sharpen = im_eq + 0.6 * dog
    sharpen = np.clip(sharpen, 0, 1)
    
    return sharpen
# 2. ¿Qué hace el gaussian_filter?
# gaussian_filter(imagen, sigma=X) aplica un filtro gaussiano:
# Es un desenfoque suave.
# Promedia cada píxel con sus vecinos, pero usando una distribución gaussiana (los vecinos más cercanos pesan más, los lejanos menos).
# sigma controla qué tanto se suaviza:
# sigma pequeño → suavizado suave, mantiene más detalle.    
# sigma grande → suavizado más fuerte, borra más detalles.

# 3. ¿Por qué restar las dos imágenes borrosas?
# dog = blur1 - blur2
# Eso se llama DoG (Difference of Gaussians).
# Idea intuitiva:
# blur1 contiene estructura general + detalles medios.
# blur2 contiene principalmente estructura general, casi sin detalles finos.
# Si haces blur1 - blur2, lo que se queda fuerte en la diferencia son los detalles y bordes, porque:
# En zonas uniformes (fondo liso), ambos blurs son parecidos → resta ≈ 0.
# En zonas de cambio brusco (bordes), las diferencias entre blur1 y blur2 son grandes.
# Por eso dog es básicamente una imagen de bordes/detalles, una especie de mapa de “dónde cambian las cosas”.
# Matemáticamente, el DoG aproxima la Laplaciana de Gauss (LoG), que es un clásico detector de bordes.

# 4. Mezclar la imagen original con los detalles (sharpen)
# sharpen = im_eq + 0.6 * dog
# Aquí estás haciendo algo muy parecido a un unsharp masking:
# Tomas la imagen original im_eq.
# Tomas una imagen que contiene detalles y bordes (dog).
# Se los sumas a la original, pero con un peso (0.6).
# Qué significa esto:
# En los bordes: dog tiene valores positivos o negativos grandes → se realza el contraste en esa zona → el borde se ve más “afilado”.
# En zonas planas: dog ≈ 0 → no cambia casi nada.
# El factor 0.6 controla qué tanto se realza:
# Si fuera más grande (1, 1.5, etc.) → la imagen se ve más nítida pero puedes meter ruido o “halo”.
# Si fuera más pequeño (0.2, 0.3) → el efecto es más suave y discreto.

# 5. ¿Por qué np.clip?
# sharpen = np.clip(sharpen, 0, 1)
# Como sumaste cosas, algunos píxeles pueden salir:
# Menores a 0 (valores negativos).
# Mayores a 1 (sobreexpuestos).
# np.clip(sharpen, 0, 1) corta todo:
# Si algo < 0 → lo pone en 0.
# Si algo > 1 → lo pone en 1.
# Así te aseguras de que la imagen siga en un rango válido para mostrarla o guardarla como imagen normal.