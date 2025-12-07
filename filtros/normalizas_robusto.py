import numpy as np

# Normalización por percentiles

# Esta función encuentra el rango útil de intensidades de una imagen usando los percentiles 1 y 99,
# elimina los valores extremos que son ruido, y normaliza ese rango a [0, 1] para obtener una imagen estable, 
# limpia y adecuada para análisis.
def normalizar_robusto(im):
    p1, p99 = np.percentile(im, (1, 99))
    im_clip = np.clip(im, p1, p99)
    im_norm = (im_clip - p1) / (p99 - p1 + 1e-8)
    return im_norm.astype(np.float32)

# 🧠 1. ¿Qué problema resuelve esta función?
# Cuando trabajas con imágenes (especialmente médicas), es muy común que:
# Existan píxeles extremadamente oscuros o extremadamente brillantes por ruido, artefactos, sobreexposición, o fallos del sensor.
# Esos valores extremos distorsionan cualquier normalización clásica (como dividir entre el valor máximo).
# La normalización por percentiles es una técnica robusta que intenta ignorar esos valores raros y quedarse con el rango “bueno” de la imagen.
# 🧩 2. Cálculo de percentiles (p1 y p99)
# p1, p99 = np.percentile(im, (1, 99))
# Esto obtiene:
# p1 → el valor bajo donde está el 1% de los píxeles más oscuros
# p99 → el valor alto donde está el 1% de los píxeles más brillantes
# ¿Por qué usar percentiles?
# ✔️ Evita que un píxel extremadamente brillante (artefacto) arruine toda la normalización.
# ✔️ Ignora los valores más extremos que normalmente son ruido.
# ✔️ Se centra en el rango tonal que realmente tiene información útil.
# Este método se usa muchísimo en radiología, satélites, microscopía, etc.
# ✂️ 3. "Clipping": recortar la imagen a ese rango
# im_clip = np.clip(im, p1, p99)
# Esto fuerza:
# Todo lo que < p1 → se convierte en p1
# Todo lo > p99 → se convierte en p99
# ¿Para qué sirve?
# 👉 Para eliminar los extremos que afectan la normalización y para que el contraste final sea más estable.
# 👉 Te asegura que la imagen queda dentro de un rango útil antes de normalizar.
# Ejemplo simple:
# Si tu imagen va de 0 a 5000 pero el contenido útil está entre 200 y 1500, el clipping elimina esos extremos exagerados.
# 🎚️ 4. Normalizar a rango [0,1]
# im_norm = (im_clip - p1) / (p99 - p1 + 1e-8)
# Esto es la fórmula clásica para llevar un valor a [0, 1]:
# El mínimo (p1) pasa a ser 0
# El máximo (p99) pasa a ser 1
# El 1e-8 evita divisiones por cero si p1 == p99 (raro pero posible en imágenes muy homogéneas).
# ✔️ 5. Convertir a float32
# return im_norm.astype(np.float32)
# Razones:
# Las operaciones de procesamiento de imágenes funcionan mucho mejor con float32.
# Reduce memoria comparado con float64.
# Es un estándar para deep learning.
