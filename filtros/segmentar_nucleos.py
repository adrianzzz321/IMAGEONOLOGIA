import numpy as np
from skimage.filters import threshold_otsu
from skimage.morphology import opening, closing, disk, remove_small_objects,label
from skimage.segmentation import watershed
from scipy.ndimage import distance_transform_edt, gaussian_filter

# Toma la imagen realzada, separa núcleos del fondo, limpia la máscara,
#  calcula la distancia al borde para cada núcleo, usa esa información para
#  crear semillas internas y aplica watershed para obtener cada núcleo bien 
# separado y etiquetado. Devuelve la máscara binaria y la imagen con los núcleos 
# numerados.

def segmentar_nucleos(im_realzada):

    th = threshold_otsu(im_realzada)
    mask = im_realzada > th

    mask = opening(mask, disk(1))
    mask = closing(mask, disk(2))
    mask = remove_small_objects(mask, min_size=70)

    dist = distance_transform_edt(mask)

    dist_smooth = gaussian_filter(dist, sigma=1.0)

    umbral_marcadores = np.percentile(dist_smooth[mask], 70)
    markers = label(dist_smooth > umbral_marcadores)


    labels_ws = watershed(-dist_smooth, markers, mask=mask)

    return mask, labels_ws


# 🧠 1. Umbralización con Otsu (separar fondo vs núcleos)
# th = threshold_otsu(im_realzada)
# mask = im_realzada > th


# threshold_otsu calcula un umbral automático que separa:

# Intensidades bajas → fondo

# Intensidades altas → núcleos (o regiones de interés)

# mask es una imagen binaria:

# True (1) → píxel considerado núcleo

# False (0) → fondo

# Es el primer corte “grueso” para saber dónde hay núcleos.

# 🧹 2. Limpieza de la máscara con morfología
# mask = opening(mask, disk(1))
# mask = closing(mask, disk(2))
# mask = remove_small_objects(mask, min_size=70)

# a) Opening (apertura)

# opening(mask, disk(1))

# Operación: erosión seguida de dilatación con un elemento estructurante disco de radio 1.

# Sirve para:

# Eliminar pequeños puntos de ruido.

# Suavizar bordes muy “dentados”.

# b) Closing (cierre)

# closing(mask, disk(2))

# Operación: dilatación seguida de erosión.

# Sirve para:

# Cerrar pequeños huecos dentro de los núcleos.

# Unir partes muy cercanas de un mismo objeto.

# c) Eliminar objetos pequeños

# mask = remove_small_objects(mask, min_size=70)

# Elimina componentes conectados con menos de 70 píxeles.

# Esto filtra:

# Ruido residual.

# Punteo que no corresponde a núcleos reales.

# Después de esto, mask es una máscara binaria mucho más limpia y coherente.

# 📏 3. Transformada de distancia
# dist = distance_transform_edt(mask)


# La distance transform (edt) calcula, para cada píxel dentro de la máscara:

# La distancia al píxel de fondo más cercano.

# Resultado:

# En el centro de cada núcleo → valores altos (lejos del borde).

# Cerca de los bordes → valores bajos.

# Esto convierte la máscara en una especie de “montaña” por cada núcleo.

# 🌫️ 4. Suavizado de la distancia
# dist_smooth = gaussian_filter(dist, sigma=1.0)


# Aplica un filtro gaussiano para suavizar la transformada de distancia.

# Reduce irregularidades y picos raros.

# Hace que cada núcleo se parezca más a una colina suave.

# Esto ayuda muchísimo para que el watershed funcione bien y no se fragmente en exceso.

# 🎯 5. Cálculo de marcadores internos
# umbral_marcadores = np.percentile(dist_smooth[mask], 70)
# markers = label(dist_smooth > umbral_marcadores)


# Aquí se crean los “semillas” para watershed:

# dist_smooth[mask] → toma solo los valores de distancia dentro de los núcleos.

# np.percentile(..., 70) → escoge un valor tal que:

# El 70% de los píxeles tienen distancia menor o igual.

# El 30% restante (los más centrales) son los puntos más lejos del borde.

# dist_smooth > umbral_marcadores → genera una máscara que marca las zonas más centrales de los núcleos.

# label(...) → etiqueta cada región conectada como un marcador distinto:

# 1, 2, 3, … → semillas para cada núcleo.

# Estos marcadores son como “banderitas” puestas dentro de cada núcleo, desde donde comenzará la expansión del watershed.

# 🌊 6. Segmentación final con watershed
# labels_ws = watershed(-dist_smooth, markers, mask=mask)


# Se aplica watershed sobre -dist_smooth:

# Como dist_smooth tiene valores altos en el centro de los núcleos, al usar -dist_smooth se convierten en valles.

# Watershed “inunda” la imagen desde los marcadores y separa regiones vecinas.

# markers define los puntos de inicio de cada región.

# mask=mask restringe el watershed solo al interior de la máscara de núcleos (no se expande al fondo).

# Resultado:

# labels_ws es una imagen de etiquetas:

# 0 → fondo

# 1, 2, 3, … → cada núcleo individualmente segmentado

# 🎁 7. Lo que devuelve la función
# return mask, labels_ws


# mask → máscara binaria de núcleos (fondo vs núcleos).

# labels_ws → versión segmentada donde cada núcleo tiene una etiqueta distinta.

# Perfecto para usar con regionprops y análisis posterior.