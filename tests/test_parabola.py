from ..libgeo.parabola import Parabola
import unittest

class TestParabola(unittest.TestCase):
  def setUp(self):
    self.parabola = Parabola(1, 2, 3)

  def test_str(self):
    self.assertEqual(str(self.parabola), "Parabola( 1x^2 + 2x + 3 )")
