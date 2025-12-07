import numpy as np
def detectar_nucleos_sospechosos(props, areas, intensidades,
                                 p_area_baja=10, p_area_alta=90, p_intensidad_alta=90):

    umbral_area_baja = np.percentile(areas, p_area_baja)
    umbral_area_alta = np.percentile(areas, p_area_alta)
    umbral_intensidad_alta = np.percentile(intensidades, p_intensidad_alta)

    nucleos_sospechosos = []

    for r in props:
        if (r.area < umbral_area_baja or
            r.area > umbral_area_alta or
            r.mean_intensity > umbral_intensidad_alta):
            nucleos_sospechosos.append(r)

    print("Núcleos sospechosos detectados:", len(nucleos_sospechosos))

    return nucleos_sospechosos

# 🧠 1. ¿Qué es lo que resuelve esta función?
# Esta función intenta identificar núcleos de células que no son normales por:
# Tener áreas demasiado pequeñas (posibles fragmentos, ruido).
# Tener áreas demasiado grandes (núcleos fusionados, atípicos o células gigantes).
# Tener intensidad media anormalmente alta (posible hiperintensidad, problemas de tinción, artefactos).
# Es decir:
# Encuentra objetos atípicos comparándolos contra el comportamiento general de la población.
# Se usa muchísimo en análisis histológico para detectar células raras o fallas en segmentación.
# 🧩 2. Umbrales basados en percentiles
# umbral_area_baja = np.percentile(areas, p_area_baja)
# umbral_area_alta = np.percentile(areas, p_area_alta)
# umbral_intensidad_alta = np.percentile(intensidades, p_intensidad_alta)
# En lugar de poner umbrales fijos, usa percentiles:
# Percentil 10 → área muy pequeña (10% más bajo de toda la distribución).
# Percentil 90 → área muy grande (10% más alto).
# Percentil 90 de intensidad → núcleos demasiado brillantes.
# ¿por qué usar percentiles?
# ✔️ Se adapta automáticamente a cada imagen.
# ✔️ No necesitas saber de antemano qué es “grande” o “pequeño”.
# ✔️ Es robusto contra variaciones entre imágenes.
# Básicamente, defines qué tan “extremo” debe ser un núcleo para considerarlo sospechoso.
# 🔍 3. Bucle de clasificación núcleo por núcleo
# for r in props:
#     if (r.area < umbral_area_baja or
#         r.area > umbral_area_alta or
#         r.mean_intensity > umbral_intensidad_alta):
#         nucleos_sospechosos.append(r)
# Cada objeto (núcleo) tiene propiedades medidas con regionprops:
# r.area
# r.mean_intensity
# Aquí aplicas lógica OR:
# Si el área < umbral_bajo → núcleo demasiado pequeño → sospechoso
# Si el área > umbral_alto → núcleo demasiado grande → sospechoso
# Si la intensidad > umbral_alto → núcleo demasiado brillante → sospechoso
# Cualquier condición que se cumpla → se considera atípico.
# Esto detecta:
# Fragmentos microscópicos mal segmentados
# Células fusionadas
# Células altamente teñidas
# Células deformes
# Ruido interpretado como núcleo
# 📊 4. Reporte del resultado
# print("Núcleos sospechosos detectados:", len(nucleos_sospechosos))
# Permite ver rápidamente si:
# La segmentación salió limpia
# Hubo mucha variabilidad
# La imagen tiene problemas de tinción o iluminación
# ✔️ 5. Retorno
# return nucleos_sospechosos
# Devuelve la lista completa de núcleos atípicos.
# Con eso puedes:
# Dibujarlos en la imagen
# Analizar sus características
# Excluirlos del cálculo estadístico
# Marcar células raras en un reporte