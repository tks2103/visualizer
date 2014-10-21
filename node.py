def prn(item):
  print(item)

def generate_midpoint(segment):
  return ( (segment[0][0] + segment[1][0]) / 2.0,
           (segment[0][1] + segment[1][1]) / 2.0 )

assert(generate_midpoint( ((0, 0), (2, 2)) ) == (1, 1))
assert(generate_midpoint( ((0, 0), (1, 1)) ) == (0.5, 0.5))

def generate_coefficients(segment):
  slope     = (segment[1][1] - segment[0][1]) / (1.0 * (segment[1][0] - segment[0][0]))
  intersect = (segment[1][1] - slope * segment[1][0])
  return (slope, intersect)

assert(generate_coefficients( ( (1, 2), (3, 4) ) ) == (1, 1) )
assert(generate_coefficients( ( (1, 3), (3, 4) ) ) == (0.5, 2.5) )

def flip_slope(coefficients):
  if coefficients[0] == 0:
    raise Exception('Divide by zero')
  return ( 1 / (-1.0 * coefficients[0]), coefficients[1] )

assert(flip_slope( (4, 5) ) == (-0.25, 5))

def calculate_intersect(coefficients, point):
  slope     = coefficients[0]
  intersect = (point[1] - slope * point[0])
  return (slope, intersect)

assert(calculate_intersect( (4, 0), (2, 5) ) == (4, -3) )
assert(calculate_intersect( (4, 0), (2, 5) ) == (4, -3) )

def perpendicular_line(segment):
  midpoint = generate_midpoint(segment)
  coefficients = generate_coefficients(segment)
  coefficients = flip_slope(coefficients)
  coefficients = calculate_intersect(coefficients, midpoint)
  return coefficients

assert(perpendicular_line( ((0, 0), (1, 1)) ) == (-1, 1) )

def horizontal_line_intersection(line, horizontal_coordinate):
  return ( (horizontal_coordinate - line[1]) / (1.0 * line[0]), horizontal_coordinate )

assert(horizontal_line_intersection( (2, 3), 5 ) == ( 1, 5 ) )

def parabola_intersection(twoPoints, point):
  return generate_midpoint((horizontal_line_intersection( perpendicular_line(twoPoints), point[1] ), generate_midpoint(twoPoints)))

def direction(twoPoints, point):
  intersection_point = parabola_intersection(twoPoints, point)
  if(point[0] < intersection_point[0]):
    return 'left'
  else:
    return 'right'

assert(direction( ((1, 2), (2, 1)), (3, 0) ) == 'right')
assert(direction( ((1, 2), (2, 1)), (0, 0) ) == 'left')

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
    if(type(self.data[0]) == int):
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

  #def insert(self, point):

    #return

node1 = Node(None, None, (1, 1))

tree = Tree(node1)
assert(tree.search((0, 0)) == (1, 1))

node3 = Node(None,  None,  (1, 2))
node5 = Node(None,  None,  (2, 1))
node6 = Node(None,  None,  (4, 3))
node4 = Node(node5, node6, ((2, 1), (4, 3)))
node2 = Node(node3, node4, ((1, 2), (2, 1)))

tree = Tree(node2)
print(tree.search((0, 0)))
assert(tree.search((0, 0)) == (2, 1))

#assert(tree.serialize() == " ((1, 1)(1, 0)) (1, 1) ((1, 0)(1, 1)) (1, 0) (1, 1) ")
