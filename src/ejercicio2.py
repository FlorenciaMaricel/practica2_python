def analizar_playlist(playlist):
    """
    Contiene funciones para encontrar la duración total de una playlist,
    infotmación de la canción más larga y la canción más corta.
    Cada canción debe tener la clave "duration"
    """
    duraciones_segundos = []

    for cancion in playlist:
        if "duration" in cancion:
            duracion_string = cancion["duration"]
            minutos_segundos = duracion_string.split(":")
            minutos = int(minutos_segundos[0])
            segundos = int(minutos_segundos[1])
            total_seg = minutos * 60 + segundos
            duraciones_segundos.append(total_seg)
        else:
            duraciones_segundos.append(0)

    total_segundos = sum(duraciones_segundos)
    total_minutos = total_segundos // 60
    segundos = total_segundos % 60
    max_i = duraciones_segundos.index(max(duraciones_segundos))
    min_i = duraciones_segundos.index(min(duraciones_segundos))

    return total_minutos, segundos, playlist[max_i], playlist[min_i]
