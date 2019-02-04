import random


def perturbar(valores, intensidad=0.05, semilla=None):
    azar = random.Random(semilla)
    return [v + azar.gauss(0, intensidad) for v in valores]


def borrar(valores, proporcion=0.2, semilla=None):
    azar = random.Random(semilla)
    return [0.0 if azar.random() < proporcion else v for v in valores]
