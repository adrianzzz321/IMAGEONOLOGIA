import numpy as np

# Revisa cada núcleo encontrado en la imagen.

# Mira qué tan grande es, qué forma tiene, qué tan oscuro es y qué tanta textura interna tiene.

# Usa todos esos datos para calcular un puntaje de rareza.

# Ordena los núcleos del más raro al más normal.

# Devuelve los primeros K, o sea los más sospechosos.

# 👉 En pocas palabras:
# Busca núcleos que se ven diferentes al resto y los marca como sospechosos.

def _robust_z(x):
    med = np.median(x)
    mad = np.median(np.abs(x - med)) + 1e-9
    return (x - med) / (1.4826 * mad)

def detectar_nucleos_sospechosos(props, areas, intensidades, K=4 ):

    feat = []
    idx_valid = []

    for i, r in enumerate(props):

        A = r.area
        if A < 70 or A > 6000:
            continue

        ecc   = r.eccentricity
        solid = r.solidity
        meanI = r.mean_intensity
        perim = getattr(r, "perimeter", 0.0)
        circ  = (4.0*np.pi*A) / (perim**2 + 1e-6)

        
        mask = r.image
        region_pixels = r.intensity_image[mask]
        var_int = np.var(region_pixels)   

        feat.append([A, ecc, solid, meanI, perim, circ, var_int])
        idx_valid.append(i)

    if not feat:
        print("No se encontraron núcleos válidos.")
        return []

    feat = np.array(feat, dtype=np.float32)

    zA      = _robust_z(feat[:, 0])
    zEcc    = _robust_z(feat[:, 1])
    zSol    = -_robust_z(feat[:, 2])
    zInt    = _robust_z(1 - feat[:, 3]) 
    zPer    = _robust_z(feat[:, 4])
    zCir    = -_robust_z(feat[:, 5])
    zVar    = _robust_z(feat[:, 6])      

    score = (0.35 * zInt +     
         0.25 * zSol +
         0.30 * zVar +     
         0.10 * zCir +
         0.05 * zEcc +
         0.03 * zA +
         0.02 * zPer)

    order = np.argsort(score)[::-1]
    K_eff = min(K, len(order))

    top_idx = [idx_valid[j] for j in order[:K_eff]]

    sospechosos = [props[j] for j in top_idx]

    print(f"Detectados como sospechosos (top {K_eff}): {K_eff}")
    print("Scores:", score[order[:K_eff]])

    return sospechosos

# 1. Función auxiliar: _robust_z(x)
# def _robust_z(x):
#     med = np.median(x)
#     mad = np.median(np.abs(x - med)) + 1e-9
#     return (x - med) / (1.4826 * mad)
# ¿Qué hace?
# x es un vector con los valores de alguna característica (área, intensidad, etc.) para todos los núcleos.
# med = np.median(x
# Calcula la mediana de esos valores, o sea el valor “central” de la distribución.
# mad = np.median(np.abs(x - med)) + 1e-9
# Calcula el MAD (Median Absolute Deviation):
# Toma la distancia absoluta de cada valor a la mediana.
# Calcula la mediana de esas distancias.
# Le suma un 1e-9 para evitar división entre cero.
# return (x - med) / (1.4826 * mad)
# Convierte cada valor en un z-score robusto, es decir:
# Cuántas “desviaciones robustas” se aleja de la mediana.
# El factor 1.4826 es para que el MAD se parezca a la desviación estándar si los datos fueran normales.
# 👉 Resultado
# Te dice, para cada núcleo, qué tan raro es respecto al resto en esa característica, pero usando medidas robustas (mediana y MAD), que aguantan mejor los outliers.
# 2. Definición de la función principa
# def detectar_nucleos_sospechosos(props, areas, intensidades, K=4 ):
# props: lista de objetos regionprops (uno por núcleo segmentado).
# areas: array con el área de cada núcleo (ya calculado afuera).
# intensidades: array con la intensidad media de cada núcleo.
# K=4: número de núcleos que quieres considerar como “top sospechosos”
# (aunque luego decidas usar 1, 4, etc.).
# 3. Inicialización de listas
#     feat = []
#     idx_valid = []
# feat: aquí se irán guardando las características numéricas (features) de cada núcleo.
# idx_valid: índices de los núcleos que aceptamos como válidos (no demasiado chicos o gigantes).
# 4. Recorrido de todos los núcleos
#     for i, r in enumerate(props):
#         A = r.area
#         if A < 70 or A > 6000:
#             continue
# Se recorre cada núcleo r con su índice i.
# Se toma el área A = r.area.
# Si el área es muy pequeña (<70) o muy grande (>6000):
# Se ignora ese núcleo (continue), porque probablemente es ruido, un fragmento o una región mal segmentada.
# 5. Extracción de características geométricas y de intensidad
#         ecc   = r.eccentricity
#         solid = r.solidity
#         meanI = r.mean_intensity
#         perim = getattr(r, "perimeter", 0.0)
#         circ  = (4.0*np.pi*A) / (perim**2 + 1e-6)
# Para cada núcleo válido se calculan:
# ecc (excentricidad):
# 0 → círculo perfecto
# Cerca de 1 → muy alargado.
# solid (solidez):
# Área del núcleo / área de su casco convexo.
# Valores cercanos a 1 → forma compacta y “rellena”.
# Valores bajos → borde muy irregular, con huecos o “mordiscos”.
# meanI (intensidad media):
# Qué tan claro u oscuro es el núcleo en la imagen procesada.
# perim (perímetro):
# Longitud del contorno del núcleo.
# circ (circularidad):
# circ
# =
# 4
# 𝜋
# 𝐴
# 𝑝
# 𝑒
# 𝑟
# 𝑖
# 𝑚
# 2
# circ=
# perim
# 2
# 4πA
# ≈1 → círculo perfecto.
# ↓ → forma más rara/irregular.
# 6. Textura interna: varianza de intensidad
#         mask = r.image
#         region_pixels = r.intensity_image[mask]
#         var_int = np.var(region_pixels)
# r.image es una máscara booleana (True donde hay núcleo, False donde no).
# r.intensity_image es el recorte de la imagen alrededor del núcleo.
# region_pixels son los píxeles de intensidad dentro del núcleo.
# var_int es la varianza de esos píxeles:
# Si la varianza es baja → núcleo con intensidad bastante uniforme (más “liso”).
# Si la varianza es alta → núcleo con mucha textura interna, grumos, heterogeneidad → típico de núcleos atípicos o malignos.
# 7. Guardar features y el índice del núcleo
#         feat.append([A, ecc, solid, meanI, perim, circ, var_int])
#         idx_valid.append(i)
# feat queda como una lista de vectores con 7 características por núcleo:
# Área
# Excentricidad
# Solidez
# Intensidad media
# Perímetro
# Circularidad
# Varianza interna
# idx_valid guarda qué índice original (i) corresponde a cada fila de feat.
# 8. Comprobación de que sí hubo núcleos válidos
#     if not feat:
#         print("No se encontraron núcleos válidos.")
#         return []
# Si la lista feat está vacía → no hay nada que analizar, se devuelve lista vacía.
# 9. Convertir features a array y sacar z-scores
#     feat = np.array(feat, dtype=np.float32)
#     zA      = _robust_z(feat[:, 0])
#     zEcc    = _robust_z(feat[:, 1])
#     zSol    = -_robust_z(feat[:, 2])
#     zInt    = _robust_z(1 - feat[:, 3]) 
#     zPer    = _robust_z(feat[:, 4])
#     zCir    = -_robust_z(feat[:, 5])
#     zVar    = _robust_z(feat[:, 6])      
# Se convierte feat en un array N x 7.
# Para cada columna se calcula un z-score robusto:
# zA → qué tan grande/pequeño es el área respecto a la mediana.
# zEcc → qué tan alargado/extraño es respecto al resto.
# zSol tiene un signo cambiado (-):
# Si solidez es baja (forma irregular), su z original sería bajo → con el “menos” se vuelve alto → más sospechoso.
# zInt usa 1 - meanI:
# Cuanto más oscuro es el núcleo, mayor es 1 - meanI.
# Luego el z-score dice qué tanto más oscuro es respecto a la mediana.
# zPer → perímetro raro (muy largo/corto para su tamaño).
# zCir también va con signo menos:
# Menor circularidad (forma rarita) → mayor score.
# zVar → qué tan extrema es la textura interna. Núcleos muy granulosos tendrán zVar alto.
# 10. Cálculo del score de rareza por núcleo
#     score = (0.35 * zInt +     
#          0.25 * zSol +
#          0.30 * zVar +     
#          0.10 * zCir +
#          0.05 * zEcc +
#          0.03 * zA +
#          0.02 * zPer)
# Aquí se construye un score global combinando todas las características:
# 0.35 * zInt → mucha importancia a hipercromasia (núcleos muy oscuros).
# 0.25 * zSol → importancia a baja solidez (bordes irregulares).
# 0.30 * zVar → MUCHA importancia a textura interna (grumos).
# 0.10 * zCir → algo de peso a forma poco circular.
# 0.05 * zEcc → algo de peso a ser muy alargado.
# 0.03 * zA → poco peso al tamaño.
# 0.02 * zPer → poco peso adicional al perímetro.