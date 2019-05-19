import unittest

from dream_engine.umbral import cruzar, histeresis


class TestUmbral(unittest.TestCase):
    def test_cruzar(self):
        self.assertTrue(cruzar(0.51))
        self.assertFalse(cruzar(0.5))

    def test_histeresis_no_parpadea(self):
        self.assertEqual(histeresis([0.56, 0.5, 0.47, 0.44]), [True, True, True, False])


if __name__ == "__main__":
    unittest.main()
