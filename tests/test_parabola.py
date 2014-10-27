from ..libgeo.parabola import Parabola
import unittest

class TestParabola(unittest.TestCase):
  def setUp(self):
    self.parabola = Parabola(1, 2, 3)

  def test_str(self):
    self.assertEqual(str(self.parabola), "Parabola( 1x^2 + 2x + 3 )")

  def test_intersection(self):
    intersections = Parabola.intersections(Parabola(1, 0, 0), Parabola(2, -3, 1))
    self.assertEqual(int(intersections*100), 38)

  def test_horizontal_intersections(self):
    intersections = Parabola.horizontal_intersections([Parabola(1, 3, 1), Parabola(1, -2, -1), Parabola(1, -5, 4)])
    self.assertEqual(intersections[0], -0.4)
    self.assertEqual(intersections[1], 5/3.0)
    intersections = Parabola.horizontal_intersections([Parabola(1, 3, 1), Parabola(2, -2, -1), Parabola(1, -5, 4)])
    self.assertEqual(int(intersections[0]*100), -37)
    self.assertEqual(int(intersections[1]*100), 119)
    intersections = Parabola.horizontal_intersections([ Parabola( 0.118317539986, 1.49152790853, 9.76356184021 ),
                                                        Parabola( 0.611349319839, 4.78624866099, 12.7268065936 ),
                                                        Parabola( 0.118317539986, 1.49152790853, 9.76356184021 ) ])
    print intersections
    self.assertEqual(int(intersections[1]*100), 119)
