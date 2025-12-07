import numpy as np
from skimage.measure import regionprops
def analizar_nucleos(labels_ws, sharpened_im):
    props = regionprops(labels_ws, intensity_image=sharpened_im)

    areas = []
    intensidades = []

    for r in props:
        areas.append(r.area)
        intensidades.append(r.mean_intensity)

    areas = np.array(areas)
    intensidades = np.array(intensidades)

    print("Número de núcleos detectados:", len(props))
    print("Área mínima:", np.min(areas))
    print("Área máxima:", np.max(areas))
    print("Área promedio:", np.mean(areas))

    return props, areas, intensidades
