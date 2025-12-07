import matplotlib.pyplot as plt
def mostrar_resultados(sharpened_im, mask, labels_ws):
    plt.figure(figsize=(10, 4))

    plt.subplot(1, 3, 1)
    plt.imshow(sharpened_im, cmap="gray")
    plt.title("Imagen Realzada")
    plt.axis("off")

    plt.subplot(1, 3, 2)
    plt.imshow(mask, cmap="gray")
    plt.title("Máscara Binaria (Otsu + morfología)")
    plt.axis("off")

    plt.subplot(1, 3, 3)
    plt.imshow(labels_ws, cmap="nipy_spectral")
    plt.title("Núcleos Segmentados (watershed)")
    plt.axis("off")

    plt.tight_layout()
    plt.show()
    