import unittest

from dream_engine.consolidacion import fusionar, repasar
from dream_engine.patrones import Patron


class TestConsolidacion(unittest.TestCase):
    def test_repasar_envejece(self):
        patrones = repasar([Patron([1.0, 0.0])], ciclos=4, semilla=1)
        self.assertEqual(patrones[0].edad, 4)

    def test_fusionar_parecidos(self):
        a = Patron([0.9, 0.1], peso=0.6)
        b = Patron([0.91, 0.1], peso=0.4)
        c = Patron([0.0, 1.0])
        self.assertEqual(len(fusionar([a, b, c])), 2)


if __name__ == "__main__":
    unittest.main()
