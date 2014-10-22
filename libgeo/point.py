class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __str__(self):
    return "Point(%s, %s)"%(self.x, self.y)

  def tup(self):
    return (self.x, self.y)
