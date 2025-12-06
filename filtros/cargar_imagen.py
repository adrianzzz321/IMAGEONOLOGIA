def cargar_imagen(ruta):
    im = imageio.imread(ruta).astype(np.float32)
    if im.ndim == 3:
        im = np.mean(im, axis=2).astype(np.uint8)
    else:
        im = im.astype(np.uint8)
    return im
