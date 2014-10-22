class Parabola:
  def __init__(self, a, b, c):
    self.a = a
    self.b = b
    self.c = c

  def __str__(self):
    return "Parabola( %sx^2 + %sx + %s )"%(str(self.a), str(self.b), str(self.c))
