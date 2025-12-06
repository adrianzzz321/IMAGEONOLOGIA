def crear_imagen_ecualizada(img_norm, cdf):
    img_u8 = (img_norm * 255).astype(np.uint8)
    img_eq = cdf[img_u8]
    return img_eq.astype(np.float32)
