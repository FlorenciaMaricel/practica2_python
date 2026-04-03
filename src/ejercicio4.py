def validar_email(email):
    """
    Valida un email según los criterios:
    - Contiene exactamente un @
    - Al menos un carácter antes del @
    - Al menos un punto después del @
    - No empieza ni termina con @ ni con .
    - La parte después del último punto tiene al menos 2 caracteres (dominio)
    """

    if email.count('@') != 1:
        return False

    lista_email = email.split('@')
    nombre = lista_email[0]
    dominio = lista_email[1]

    if len(nombre) == 0:
        return False

    if '.' not in dominio:
        return False

    if email[0] in ['@', '.'] or email[-1] in ['@', '.']:
        return False

    ultima_parte = dominio.split('.')[-1]

    if len(ultima_parte) < 2:
        return False

    return True
