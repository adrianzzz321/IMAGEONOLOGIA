Mejora de calidad de imagen y aplicación de IA para la detección de lesiones cervicales en muestras citológicas

🏫 Universidad Católica Boliviana “San Pablo” – Sede Tarija

Carrera: Ingeniería Biomédica
Materia: INB-235 Imagenología Médica
Estudiantes:
Aracely Melva Zubieta Morales
Jorge Adrian Alanoca Riveros
Joaquín Ignacio Aguirre Bustos
Docente: Ing. Noelia Mendoza Zenteno
Año: 2025

📄 Descripción del Proyecto

Este repositorio contiene el desarrollo del proyecto académico Imagenología Médica, cuyo objetivo principal es mejorar la calidad de imágenes microscopias citológicas provenientes de frotis cervicales, y aplicar modelos de inteligencia artificial para apoyar el diagnóstico temprano del cáncer de cuello uterino.

El proyecto integra técnicas de:
Preprocesamiento avanzado de imágenes
Corrección de iluminación
Reducción de ruido
Ecualización y realce
Segmentación de núcleos
Detección de patrones celulares atípicos mediante IA
Las herramientas se implementan principalmente en Python, utilizando librerías de procesamiento digital de imágenes.

🎯 Objetivo General

Desarrollar un sistema que mejore la calidad de imágenes microscópicas de placas citológicas y permita la detección de patrones celulares asociados al cáncer de cuello uterino mediante IA.

🎯 Objetivos Específicos

1. Crear una base de datos de imágenes citológicas.
2. Implementar un algoritmo de mejora de calidad y definición de bordes celulares.
3. Desarrollar modelos de IA para detectar patrones de riesgo.
4. Integrar el flujo completo en un sistema funcional.
5. Evaluar el desempeño, precisión y limitaciones del sistema.

📚 Contenido del Repositorio

/src/ – Scripts de procesamiento de imágenes (normalización, filtrado, segmentación).
/notebooks/ – Jupyter Notebooks con experimentación y análisis.
/data/ – Carpeta para dataset de imágenes (no incluida por privacidad).
/docs/ – Documentación, reportes y diagramas.
README.md – Documento principal del proyecto.
requirements.txt – Dependencias requeridas.

🧪 Metodología

1. Carga y preprocesamiento de imágenes

Conversión a escala de grises

Normalización por percentiles (1–99)

Corrección de iluminación (shading correction)

Eliminación de ruido (mediana + Gaussiano)

Ecualización del histograma

2. Realce de bordes y estructuras celulares

Difference of Gaussians (DoG)

Filtros de sharpening controlado

3. Segmentación de núcleos celulares

Umbralización adaptativa

Operaciones morfológicas

Etiquetado de regiones y extracción de propiedades

4. Inteligencia Artificial

Entrenamiento preliminar de modelos para detección de atipias

Métricas: precisión, sensibilidad, especificidad

5. Visualización y evaluación

Comparación antes/después del procesamiento

Identificación visual de núcleos atípicos

Reportes gráficos y métricos

🛠️ Tecnologías Utilizadas

Python 3.x

NumPy

OpenCV

Scikit-image

SciPy

Matplotlib

Scikit-learn / TensorFlow (para IA)

📊 Resultados (Resumen)

El proyecto logró:

Mejoras evidentes en contraste y delimitación de bordes celulares.

Corrección exitosa de iluminación desigual típica de microscopía.

Segmentación adecuada de núcleos en varias muestras.

Potencial aplicación en la detección temprana de lesiones intraepiteliales.

