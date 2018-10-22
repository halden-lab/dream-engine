import math
from dataclasses import dataclass
from typing import List


@dataclass
class Patron:
    valores: List[float]
    peso: float = 1.0
    edad: int = 0

    def energia(self):
        return math.sqrt(sum(v * v for v in self.valores)) * self.peso


def normalizar(valores):
    total = math.sqrt(sum(v * v for v in valores)) or 1.0
    return [v / total for v in valores]


def similitud(a, b):
    return sum(x * y for x, y in zip(normalizar(a), normalizar(b)))


def persistir(patrones, minimo=0.05):
    return [p for p in patrones if p.energia() >= minimo]
