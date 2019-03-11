from .consolidacion import fusionar, repasar
from .patrones import persistir
from .umbral import cruzar


class Motor:
    def __init__(self, ciclos=3, semilla=None):
        self.ciclos = ciclos
        self.semilla = semilla
        self.memoria = []
        self.noches = 0

    def recordar(self, patron):
        self.memoria.append(patron)

    def dormir(self):
        repasados = repasar(self.memoria, self.ciclos, semilla=self.semilla)
        self.memoria = persistir(fusionar(repasados))
        self.noches += 1
        return len(self.memoria)

    def despierto(self):
        if not self.memoria:
            return False
        return cruzar(sum(p.peso for p in self.memoria) / len(self.memoria))
