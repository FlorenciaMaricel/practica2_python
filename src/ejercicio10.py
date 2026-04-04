"""" Modúlo que analiza una competencia de cocina
"""

def competencia_cocina(rounds):
    """
    Simula una competencia de cocina con múltiples rondas.
    Calcula puntajes, ganadores y estadísticas acumuladas por participante.
    Imprime resultados por ronda y retorna la tabla final ordenada por puntaje total.
    """
    estadisticas = {}

    for i, ronda in enumerate(rounds, start=1):
        print(f"\nRonda {i} - {ronda['theme']}:")

        puntajes_ronda = {}

        for nombre, jueces in ronda['scores'].items():
            puntaje = sum(jueces.values())
            puntajes_ronda[nombre] = puntaje

            if nombre not in estadisticas:
                estadisticas[nombre] = {
                    'total': 0,
                    'wins': 0,
                    'best': 0,
                    'rounds': 0
                }

            estadisticas[nombre]['total'] += puntaje
            estadisticas[nombre]['rounds'] += 1

            if puntaje > estadisticas[nombre]['best']:
                estadisticas[nombre]['best'] = puntaje

        ganador = max(puntajes_ronda, key=puntajes_ronda.get)
        estadisticas[ganador]['wins'] += 1

        print(f"  Ganador: {ganador} ({puntajes_ronda[ganador]} pts)")

        print(f"{'Cocinero':<15} {'Puntos':<10}")
        for nombre, puntos in puntajes_ronda.items():
            print(f"{nombre:<15} {puntos:<10}")

    tabla = []

    for nombre, datos in estadisticas.items():
        promedio = datos['total'] / datos['rounds']
        tabla.append((nombre, datos['total'], datos['wins'], datos['best'], promedio))

    tabla.sort(key=lambda x: x[1], reverse=True)

    return tabla
