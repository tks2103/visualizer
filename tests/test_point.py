from ..libgeo.point import Point
import unittest

class TestPoint(unittest.TestCase):
  def setUp(self):
    self.point = Point(1, 1)

  def test_str(self):
    self.assertEqual(str(self.point), "Point(1, 1)")

  def test_tup(self):
    self.assertEqual(self.point.tup(), (1, 1))
