from point import Point
from line import Line

class Segment:
  def __init__(self, start, end):
    self.start  = start
    self.end    = end

  def __str__(self):
    return "Segment( %s, %s )"%(str(self.start), str(self.end))

  def midpoint(self):
    return Point( (self.start.x + self.end.x) / 2.0,
                  (self.start.y + self.end.y) / 2.0 )

  def to_line(self):
    slope     = (self.end.y - self.start.y) / (1.0 * (self.end.x - self.start.x))
    intersect = (self.end.y - slope * self.end.x)
    return Line(slope, intersect)

  def tup(self):
    return (self.start.tup(), self.end.tup())

  def perpendicular_line_to_midpoint(self):
    line = self.to_line()
    line.perpendicularize()
    line.shift_intercept(self.midpoint())
    return line
