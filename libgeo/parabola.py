from libgeo.segment import Segment
from libgeo.point   import Point

class Parabola:
  @staticmethod
  def generate_from_directrix_and_focus(directrix, focus):
    a = 1 / (1.0 * 2 * focus.y - 2 * directrix)
    b = -(2 * focus.x) / (1.0 * 2 * focus.y - 2 * directrix)
    c = (focus.x * focus.x + focus.y * focus.y - directrix * directrix) / (1.0 * 2 * focus.y - 2 * directrix)
    return Parabola(a, b, c)

  def __init__(self, a, b, c):
    self.a = a
    self.b = b
    self.c = c

  def at(self, x):
    return x * x * self.a + x * self.b + self.c

  def segments(self, width):
    points = [Point(x, self.at(x)) for x in range(-width/2, width/2+2)]
    return [Segment(*x) for x in zip(points, points[1:])]

  def __str__(self):
    return "Parabola( %sx^2 + %sx + %s )"%(str(self.a), str(self.b), str(self.c))
