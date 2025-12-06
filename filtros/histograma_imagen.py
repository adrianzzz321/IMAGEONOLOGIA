def histograma_imagen(img_u8):
    hist = ndi.histogram(img_u8, min=0, max=256, bins=256)
    return hist
