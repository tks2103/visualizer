def prn(item):
  print(item)

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

  def insert(self, point):
    return

node1 = Node(None, None, (1,1))

tree = Tree(node1)
tree.insert((1, 0))
assert(tree.serialize() == " ((1, 1)(1, 0)) (1, 1) ((1, 0)(1, 1)) (1, 0) (1, 1) ")
