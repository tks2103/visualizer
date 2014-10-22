from ..libgeo.segment import Segment
from ..libgeo.point import Point
import unittest

class TestSegment(unittest.TestCase):
  def setUp(self):
    self.segment = Segment(Point(1, 1), Point(2, 2))

  def test_str(self):
    self.assertEqual(str(self.segment), "Segment( Point(1, 1), Point(2, 2) )")

  def test_midpoint(self):
    midpoint = self.segment.midpoint()
    self.assertEqual(midpoint.x, 1.5)
    self.assertEqual(midpoint.y, 1.5)

  def test_to_line(self):
    line = self.segment.to_line()
    self.assertEqual(line.slope, 1.0)
    self.assertEqual(line.intercept, 0)

  def test_perpendicular_line_to_midpoint(self):
    line = self.segment.perpendicular_line_to_midpoint()
    self.assertEqual(line.slope, -1.0)
    self.assertEqual(line.intercept, 3.0)
