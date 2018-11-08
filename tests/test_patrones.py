import unittest

from dream_engine.patrones import Patron, persistir, similitud


class TestPatrones(unittest.TestCase):
    def test_similitud_consigo_mismo(self):
        self.assertAlmostEqual(similitud([0.3, 0.4], [0.3, 0.4]), 1.0)

    def test_similitud_ortogonal(self):
        self.assertAlmostEqual(similitud([1, 0], [0, 1]), 0.0)

    def test_persistir_descarta_lo_debil(self):
        fuerte = Patron([0.9, 0.2])
        debil = Patron([0.01, 0.0], peso=0.5)
        self.assertEqual(persistir([fuerte, debil]), [fuerte])


if __name__ == "__main__":
    unittest.main()
