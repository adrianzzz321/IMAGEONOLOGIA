
# Suma acumulada del histograma para saber cuántos píxeles van hasta cada intensidad,
#  y la normaliza a 0–1 para usarla en ecualización.
def conseguir_cdf(hist):
    cdf = hist.cumsum()
    cdf = cdf / cdf[-1]
    return cdf

# 🧠 1. ¿Qué es hist?

# hist es un histograma de intensidades de una imagen.
# Es decir:

# Cada posición del arreglo representa un nivel de intensidad (0–255, por ejemplo).

# Cada valor es cuántos píxeles tienen esa intensidad.

# Ejemplo simple:
# hist[50] = 1200 significa que hay 1200 píxeles con intensidad 50.

# 🧩 2. Cálculo de la CDF (Cumulative Distribution Function)
# cdf = hist.cumsum()


# cumsum() significa suma acumulativa.

# La CDF responde a:

# ¿Cuántos píxeles tienen intensidad menor o igual a un valor dado?

# Ejemplo:
# Si cdf[100] = 5000, quiere decir que 5000 píxeles tienen valores entre 0 y 100.

# ¿Por qué se usa la CDF?

# La CDF es fundamental en ecualización de histograma, porque permite redistribuir las intensidades para mejorar el contraste.

# 📏 3. Normalización de la CDF
# cdf = cdf / cdf[-1]


# cdf[-1] es el último valor de la CDF, o sea:

# El total de píxeles en la imagen.

# Al dividir:

# La CDF pasa a estar entre 0 y 1.

# La última intensidad ahora vale 1.0 → representa el 100% de la distribución.

# ¿Por qué normalizar?

# ✔️ Permite mapear intensidades de manera uniforme.
# ✔️ Se convierte en una función acumulada proporcional.
# ✔️ Es indispensable para ecualizar correctamente una imagen.

# Con esta normalización, puedes usar:

# nueva_intensidad = cdf[intensidad_original] * 255


# Y eso realza el contraste de forma automática.

# 🔧 4. Resultado

# La función devuelve un vector donde:

# cdf[i] indica qué proporción de píxeles tienen intensidad ≤ i.

# El rango siempre es 0 → 1.