def calcular_envio(peso, zona):
    """
    Calcula el costo de envío según el peso (kg) y la zona.
    """
    zona = zona.lower()

    if zona not in ["local", "regional", "nacional"]:
        return "Zona no válida. Las zonas disponibles son: local, regional, nacional."

    if peso <= 1:
        if zona == "local":
            return 500
        if zona == "regional":
            return 1000
        return 2000

    if peso <= 5:
        if zona == "local":
            return 1000
        if zona == "regional":
            return 2500
        return 4500

    if zona == "local":
        return 2000
    if zona == "regional":
        return 5000
    return 8000
