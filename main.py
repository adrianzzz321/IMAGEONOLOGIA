from filtros import *
import numpy as np

im = cargar_imagen("Data\imagendecelula2.jpg")
im_norm = normalizar_robusto(im)
im_corr = corregir_iluminacion(im_norm)
im_denoise = denoise_imagen(im_corr)

img_u8 = (im_denoise * 255).astype(np.uint8)
hist = histograma_imagen(img_u8)
cdf = conseguir_cdf(hist)
im_ecualizada = crear_imagen_ecualizada(im_denoise, cdf)

sharpened_im = realzar_imagen(im_ecualizada)
mask, labels_ws = segmentar_nucleos(sharpened_im)

mostrar_resultados(sharpened_im, mask, labels_ws)
props, areas, intensidades = analizar_nucleos(labels_ws, sharpened_im)
mostrar_histograma_areas(areas, bins=20)
nucleos_sospechosos = detectar_nucleos_sospechosos(props, areas, intensidades)
marcar_nucleos_sospechosos(im, nucleos_sospechosos)