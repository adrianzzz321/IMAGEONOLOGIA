def segmentar_nucleos(im_realzada):

    th = threshold_otsu(im_realzada)
    mask = im_realzada > th

    mask = opening(mask, disk(1))
    mask = closing(mask, disk(2))
    mask = remove_small_objects(mask, min_size=70)

    dist = distance_transform_edt(mask)

    dist_smooth = gaussian_filter(dist, sigma=1.0)

    umbral_marcadores = np.percentile(dist_smooth[mask], 70)
    markers = label(dist_smooth > umbral_marcadores)


    labels_ws = watershed(-dist_smooth, markers, mask=mask)

    return mask, labels_ws
