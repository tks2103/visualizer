from point import Point

class Line:
  def __init__(self, slope, intercept):
    self.slope      = slope
    self.intercept  = intercept

  def __str__(self):
    return "Line y = %sx + %s"%(self.slope, self.intercept)

  def perpendicularize(self):
    if self.slope == 0:
      raise Exception('Divide by zero')
    self.slope = 1 / (-1.0 * self.slope)

  def shift_intercept(self, point):
    self.intercept = (point.y - self.slope * point.x)

  def intersection_with_horizontal(self, ycoord):
    return Point( (ycoord - self.intercept) / (1.0 * self.slope), ycoord )
