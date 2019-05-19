UMBRAL = 0.5


def cruzar(nivel, umbral=UMBRAL):
    return nivel > umbral


def histeresis(niveles, subir=0.55, bajar=0.45):
    estado = False
    trazas = []
    for nivel in niveles:
        if not estado and nivel > subir:
            estado = True
        elif estado and nivel < bajar:
            estado = False
        trazas.append(estado)
    return trazas
