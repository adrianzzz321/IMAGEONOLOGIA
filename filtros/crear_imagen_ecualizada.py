import numpy as np

# Convierte la imagen a valores 0–255, usa la CDF para reemplazar cada intensidad
#  y así mejorar el contraste, y devuelve la imagen ecualizada lista para 
# seguir procesando.

def crear_imagen_ecualizada(img_norm, cdf):
    img_u8 = (img_norm * 255).astype(np.uint8)
    img_eq = cdf[img_u8]
    return img_eq.astype(np.float32)

# 🧠 1. ¿Qué hace esta función?

# Esta función aplica ecualización de histograma, pero en una forma muy eficiente:

# Usa la CDF (función de distribución acumulada) ya calculada.

# Reemplaza cada intensidad por su valor acumulado.

# Mejora el contraste de la imagen.

# La imagen resultante tiene un rango de intensidades más distribuido y por lo tanto resalta mejor estructuras importantes como núcleos.

# 🧩 2. Convertir la imagen normalizada (0–1) a formato 0–255
# img_u8 = (img_norm * 255).astype(np.uint8)


# Tu imagen img_norm está en rango [0,1].

# Para poder usar la CDF como mapa, primero hay que pasarla a índices 0–255:

# Multiplicar por 255 → escala la imagen a intensidades tipo imagen digital tradicional.

# Convertir a uint8 → valores enteros entre 0 y 255.

# Esto convierte cada píxel en un índice válido para acceder a cdf.

# 🧩 3. Aplicar la ecualización usando indexación directa
# img_eq = cdf[img_u8]


# Este paso es clave.

# cdf es un arreglo de tamaño 256.

# img_u8 contiene valores entre 0 y 255.

# Reemplaza cada píxel por el valor de la CDF correspondiente.

# Ejemplo:

# Si un píxel tenía intensidad 50:

# nuevo_valor = cdf[50]


# Gracias a la CDF:

# Intensidades comunes se reparten más.

# Intensidades poco frecuentes se expanden.

# El contraste global mejora.

# Esto hace que regiones oscuras y brillantes se separen mejor visualmente.

# 🎨 ¿Qué representa img_eq?

# Es una imagen:

# Con contraste mejorado.

# Con intensidades en rango [0,1].

# Lista para pasos siguientes como realce o segmentación.

# 📌 4. Convertir a float32
# return img_eq.astype(np.float32)


# Esto prepara la imagen para los pasos posteriores del pipeline (sharpening, segmentación, etc.), que trabajan mejor en formato flotante.