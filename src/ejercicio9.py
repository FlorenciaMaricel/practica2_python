def limpiar_y_normalizar_alumnos(students):
    """
    Recibe una lista de diccionarios con alumnos y devuelve la lista
    limpia, normalizada, sin duplicados (se queda con la nota más alta)
    y ordenada alfabéticamente por nombre.
    """

    estados = ["aprobado", "desaprobado", "ausente"]
    alumnos_dict = {}

    for alumno in students:

        nombre = alumno.get('name')
        nota = alumno.get('grade')
        estado = alumno.get('status')

        if (not nombre or not nombre.strip() or
            not nombre.replace(" ", "").isalpha() or
            not nota or not nota.isnumeric() or
            not estado or not estado.strip() or
            estado.strip().lower() not in estados):
            continue

        nombre_n = nombre.strip().title()
        nota_n = int(nota)
        estado_n = estado.strip().title()

        if nombre_n in alumnos_dict:
            if nota_n > alumnos_dict[nombre_n]['grade']:
                alumnos_dict[nombre_n] = {'grade': nota_n, 'status': estado_n}
        else:
            alumnos_dict[nombre_n] = {'grade': nota_n, 'status': estado_n}

    alumnos_final = sorted(alumnos_dict.items())
    return alumnos_final
