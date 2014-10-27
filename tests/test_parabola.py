from ..libgeo.parabola import Parabola
import unittest

class TestParabola(unittest.TestCase):
  def setUp(self):
    self.parabola = Parabola(1, 2, 3)

  def test_str(self):
    self.assertEqual(str(self.parabola), "Parabola( 1x^2 + 2x + 3 )")

  def test_intersection(self):
    intersections = Parabola.intersections(Parabola(1, 0, 0), Parabola(2, -3, 1))
    self.assertEqual(int(intersections[0]*100), 38)
    self.assertEqual(int(intersections[1]*100), 261)
