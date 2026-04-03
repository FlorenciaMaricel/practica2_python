def ocultar_spoilers(review, spoilers):
    """
    Reemplaza palabras de spoilers por asteriscos
    """
    palabras = review.split()
    spoilers_lower = [p.lower() for p in spoilers]

    review_modificada = []

    for palabra in palabras:
        palabra_sola = palabra.strip(".,!?")
        if palabra_sola.lower() in spoilers_lower:
            censurada = "*" * len(palabra_sola)
            censurada += palabra[len(palabra_sola):]
            review_modificada.append(censurada)
        else:
            review_modificada.append(palabra)

    review_final = ""
    for palabra in review_modificada:
        review_final += palabra + " "
    review_final = review_final.strip()

    return review_final

def formatear_lineas(texto, ancho=80):
    lineas = []
    for i in range(0, len(texto), ancho):
        lineas.append(texto[i:i+ancho])
    return lineas
