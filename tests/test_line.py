from ..libgeo.line import Line
from ..libgeo.point import Point
import unittest

class TestLine(unittest.TestCase):
  def setUp(self):
    self.line = Line(5, 4)

  def test_str(self):
    self.assertEqual(str(self.line), "Line y = 5x + 4")

  def test_perpendicularize(self):
    self.line.perpendicularize()
    self.assertEqual(self.line.slope, -0.2)

  def test_shift_intercept(self):
    self.line.shift_intercept(Point(0, 0))
    self.assertEqual(self.line.intercept, 0)
    self.assertEqual(self.line.slope, 5)

  def test_intersection_with_horizontal(self):
    point = self.line.intersection_with_horizontal(4)
    self.assertEqual(point.x, 0)
    self.assertEqual(point.y, 4)
