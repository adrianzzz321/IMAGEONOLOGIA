def corregir_iluminacion(im_norm, sigma=60):
   
    fondo = gaussian_filter(im_norm, sigma=sigma)
    corr = im_norm / (fondo + 1e-8)
    return np.clip(corr, 0, 1)
