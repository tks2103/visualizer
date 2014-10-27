from libgeo.segment import Segment
from libgeo.point   import Point
from math           import sqrt

class Parabola:
  @staticmethod
  def generate_from_directrix_and_focus(directrix, focus):
    a = 1 / (1.0 * 2 * focus.y - 2 * directrix)
    b = -(2 * focus.x) / (1.0 * 2 * focus.y - 2 * directrix)
    c = (focus.x * focus.x + focus.y * focus.y - directrix * directrix) / (1.0 * 2 * focus.y - 2 * directrix)
    return Parabola(a, b, c)


  @staticmethod
  def horizontal_intersections(parabolas, start, end):
    intersect_tuples = map(lambda x: Parabola.intersections(x[0], x[1]), zip(parabolas, parabolas[1:]))
    intersects = []
    for tup in intersect_tuples:
      if min(tup) > start:
        start = min(tup)
        intersects.append(min(tup))
      else:
        start = max(tup)
        intersects.append(max(tup))
    return intersects

  @staticmethod
  def intersections(parabola1, parabola2):
    a = parabola1.a - parabola2.a
    b = parabola1.b - parabola2.b
    c = parabola1.c - parabola2.c
    if a == 0:
      return -c / (1.0 * b)
    tup = ( (-b + sqrt(b * b - 4 * a * c)) / (2 * a), (-b - sqrt(b * b - 4 * a * c)) / (2 * a) )
    return tup

  def __init__(self, a, b, c):
    self.a = a
    self.b = b
    self.c = c

  def at(self, x):
    return x * x * self.a + x * self.b + self.c

  def segments(self, start, finish):
    points = [Point(x, self.at(x)) for x in (map (lambda x: x / 10.0, range(int(start * 10), int(finish * 10))))]
    return [Segment(*x) for x in zip(points, points[1:])]

  def __str__(self):
    return "Parabola( %sx^2 + %sx + %s )"%(str(self.a), str(self.b), str(self.c))
