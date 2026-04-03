import random

def sortear_amigo_invisible(entrada):

    nombres = [nombre.strip() for nombre in entrada.split(",")]

    if not all(nombre.replace(" ", "").isalpha() for nombre in nombres):
        return "Cada nombre debe contener solo letras y no puede estar vacío."

    if len(nombres) < 3:
        return "Debe haber al menos 3 participantes."

    nombres_low = [nombre.lower() for nombre in nombres]

    if len(nombres_low) != len(set(nombres_low)):
        return "No debe haber nombres duplicados."

    participantes = tuple(nombres)

    while True:
        disponibles = list(participantes)
        asignaciones = []

        for p in participantes:
            opciones = list(filter(lambda x: x != p, disponibles))
            if not opciones:
                break
            elegido = random.choice(opciones)
            asignaciones.append(elegido)
            disponibles.remove(elegido)

        if len(asignaciones) == len(participantes):
            break

    return participantes, asignaciones
