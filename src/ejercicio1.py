def contar_lineas(texto):
    return len(texto.split(".\n"))


def contar_palabras(texto):
    return len(texto.split())


def promedio_palabras_por_linea(texto):
    lineas = len(texto.split(".\n"))
    if lineas == 0:
        return 0
    palabras = len(texto.split())
    return palabras / lineas

def lineas_encima_promedio(texto):
    promedio = promedio_palabras_por_linea(texto)
    return [linea for linea in texto.split("\n") if len(linea.split()) > promedio]