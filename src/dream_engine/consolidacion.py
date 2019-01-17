import random

from .patrones import Patron, similitud


def repasar(patrones, ciclos=3, decaimiento=0.9, semilla=None):
    azar = random.Random(semilla)
    for _ in range(ciclos):
        for patron in patrones:
            patron.edad += 1
            patron.peso *= decaimiento
        if patrones:
            elegido = azar.choice(patrones)
            elegido.peso = min(1.0, elegido.peso / decaimiento ** 2)
    return patrones


def fusionar(patrones, parecido=0.92):
    resultado = []
    for patron in patrones:
        for otro in resultado:
            if similitud(patron.valores, otro.valores) >= parecido:
                otro.peso = min(1.0, otro.peso + patron.peso / 2)
                otro.edad = max(otro.edad, patron.edad)
                break
        else:
            resultado.append(Patron(list(patron.valores), patron.peso, patron.edad))
    return resultado
