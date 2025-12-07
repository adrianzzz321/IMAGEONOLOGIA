import matplotlib.pyplot as plt
def mostrar_histograma_areas(areas, bins=20):
    plt.figure()
    plt.hist(areas, bins=bins)
    plt.title("Distribución de áreas de núcleos")
    plt.xlabel("Área (píxeles)")
    plt.ylabel("Frecuencia")
    plt.show()