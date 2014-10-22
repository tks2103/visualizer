from libgeo.point   import Point
from libgeo.segment import Segment
from libgeo.line    import Line

def prn(item):
  print item

def parabola_intersection(segment, point):
  print str(segment)
  print str(point)
  perpendicular = segment.perpendicular_line_to_midpoint()
  print str(perpendicular)
  horizontal_intersection = perpendicular.intersection_with_horizontal(point.y)
  parabola_segment = Segment(horizontal_intersection, segment.midpoint())
  return parabola_segment.midpoint()

def direction(segment, point):
  intersection_point = parabola_intersection(segment, point)
  if(point.x < intersection_point.x):
    return 'left'
  else:
    return 'right'

class Node:
  def __init__(self, left, right, data):
    self.left = left
    self.right = right
    self.data = data
    self.queuePtr = None
    self.voronoiEdgePtr = None

  def postTraversal(self, visitor):
    if(self.left):
      self.left.postTraversal(visitor)
    if(self.right):
      self.right.postTraversal(visitor)
    visitor(self.data)

  def isLeaf(self):
    if(self.data == None):
      raise Exception('called leaf on empty node')
    if(self.data.__class__.__name__ == "Point"):
      return True
    else:
      return False

  def search(self, point):
    if(self.isLeaf()):
      return self.data
    else:
      if(direction(self.data, point) == 'left'):
        return self.left.search(point)
      else:
        return self.right.search(point)

class Tree:
  def __init__(self, root):
    self.root = root

  def postTraversal(self, visitor = prn):
    self.root.postTraversal(visitor)

  def serialize(self):
    self.serializedState = ""
    self.postTraversal(self.serializerHelper)
    return self.serializedState

  def serializerHelper(self, item):
    self.serializedState += str(item);

  def search(self, point):
    return self.root.search(point)

node1 = Node(None, None, Point(1, 1))

tree = Tree(node1)

node3 = Node(None,  None,  Point(1, 2))
node5 = Node(None,  None,  Point(2, 1))
node6 = Node(None,  None,  Point(4, 3))
node4 = Node(node5, node6, Segment(Point(2, 1), Point(4, 3)))
node2 = Node(node3, node4, Segment(Point(1, 2), Point(2, 1)))

tree = Tree(node2)
print(tree.search(Point(0, -10)))
#assert(tree.serialize() == " ((1, 1)(1, 0)) (1, 1) ((1, 0)(1, 1)) (1, 0) (1, 1) ")
