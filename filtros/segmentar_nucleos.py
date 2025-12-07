import numpy as np
from skimage.filters import threshold_otsu
from skimage.morphology import opening, closing, disk, remove_small_objects,label
from skimage.segmentation import watershed
from scipy.ndimage import distance_transform_edt, gaussian_filter

# 🟪 EXPLICACIÓN SÚPER SIMPLE del segmento principal

# Si el núcleo es muy oscuro, el puntaje sube.

# Si tiene bordes raros, el puntaje sube.

# Si su interior tiene manchitas o grumos (textura alta), el puntaje sube MUCHO.

# Si la forma no es redonda, también sube.

# Combina todo eso y elige los más extraños.

#👉 Es básicamente un "detector de núcleos raros", usando varias señales sencillas.

from skimage.filters import threshold_otsu
from skimage.morphology import disk, opening, closing, remove_small_objects
from scipy.ndimage import distance_transform_edt, gaussian_filter
from skimage.segmentation import watershed
from skimage.measure import label
import numpy as np

def segmentar_nucleos(im_realzada):
    
    # 1) Invertimos la imagen → núcleos quedan brillantes
    inv = 1 - im_realzada

    # 2) Umbral Otsu sobre la imagen invertida
    th = threshold_otsu(inv)
    mask = inv > th

    # 3) Abrimos para eliminar manchas pequeñas
    mask = opening(mask, disk(1))

    # 4) Quitamos ruido menor a 50 px
    mask = remove_small_objects(mask, min_size=50)

    # 5) Transformada de distancia en máscaras brillantes (núcleos invertidos)
    dist = distance_transform_edt(mask)
    dist = gaussian_filter(dist, sigma=1)

    # 6) Cálculo de marcadores: usamos un percentil alto
    marker_th = np.percentile(dist[mask], 75)
    markers = label(dist > marker_th)

    # 7) Watershed para separar núcleos pegados
    labels_ws = watershed(-dist, markers, mask=mask)

    return mask, labels_ws


# 1) Invertimos la imagen → núcleos quedan brillantes
# inv = 1 - im_realzada


# Muchos algoritmos funcionan mejor cuando los objetos de interés son brillantes.

# Los núcleos en H&E suelen ser oscuros, por eso los invertimos.

# Si antes era oscuro (0.2), ahora pasa a 0.8 → más fácil detectarlo.

# Esto prepara la imagen para umbralización y watershed.

# 2) Umbral Otsu sobre la imagen invertida
# th = threshold_otsu(inv)
# mask = inv > th


# Otsu encuentra un umbral automático separando dos grupos de intensidades:

# píxeles brillantes → núcleos

# píxeles oscuros → fondo

# Aquí trabajamos sobre la imagen invertida, así que:

# inv > th produce una máscara donde los núcleos quedan True.

# 3) Apertura morfológica
# mask = opening(mask, disk(1))


# La “apertura” (opening) hace dos cosas:

# Erosiona ligeramente → elimina puntos sueltos y ruido fino

# Diluye después → restaura el tamaño

# Sirve para:

# Limpiar imperfecciones pequeñas

# Suavizar bordes

# El disk(1) es un elemento estructurante muy pequeño → cambios suaves.

# 4) Eliminar objetos pequeños (ruido)
# mask = remove_small_objects(mask, min_size=50)


# Descarta todo lo que no mida mínimo 50 píxeles.

# Esto elimina:

# Granos de ruido

# Artefactos microscópicos

# Trozos de células rotas muy pequeños

# 5) Transformada de distancia
# dist = distance_transform_edt(mask)
# dist = gaussian_filter(dist, sigma=1)

# ¿Qué es la transformada de distancia?

# Para cada píxel dentro de un objeto (núcleo), mide:

# “¿cuán lejos está del borde más cercano?”

# Esto logra que:

# El centro del núcleo tenga un valor alto

# El borde cercano a 0

# Es perfecto para separar núcleos pegados.

# Luego se suaviza (gaussian_filter) para evitar que el watershed genere bordes irregulares.

# 6) Marcadores basados en percentil 75 del distance transform
# marker_th = np.percentile(dist[mask], 75)
# markers = label(dist > marker_th)


# Aquí se buscan los “máximos locales” de la transformada de distancia:

# Si tomas el percentil 75, te quedas con los valores más altos → los centros de los núcleos.

# dist > marker_th marca las zonas que pertenecen a los centros.

# label() asigna números consecutivos a cada marcador.

# Estos marcadores guían el watershed.

# 7) Aplicar watershed para separar núcleos pegados
# labels_ws = watershed(-dist, markers, mask=mask)

# Por qué -dist ?

# Porque watershed segmenta cuencas, no montañas.
# Al invertir la transformada de distancia (-dist):

# Las zonas altas (centros) se vuelven “valles”.

# Watershed crece desde esos centros hasta llenar los objetos.

# Resultado:

# Cada objeto (núcleo) recibe un ID distinto.

# Núcleos pegados se separan correctamente.

# 8) Devolver la máscara y las etiquetas
# return mask, labels_ws


# mask: binaria (núcleo vs fondo)

# labels_ws: matriz con números enteros, cada uno representando un núcleo distinto.