from libgeo.parabola  import Parabola
from libgeo.segment   import Segment

class Node:
  def __init__(self, left, right, data):
    self.left = left
    self.right = right
    self.data = data

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
      return self
    else:
      parabola1 = Parabola.generate_from_directrix_and_focus(point.y, self.data.start)
      parabola2 = Parabola.generate_from_directrix_and_focus(point.y, self.data.end)
      nearest_parabola = point.nearest_vertical_parabola([parabola1, parabola2])
      if(nearest_parabola == parabola1):
        return self.left.search(point)
      else:
        return self.right.search(point)

  def insert(self, tree):
    self.left = tree.root.left
    self.right = tree.root.right
    self.data = tree.root.data

class Tree:
  def __init__(self, root):
    self.root = root

  def postTraversal(self, visitor):
    self.root.postTraversal(visitor)

  def serialize(self):
    if self.root == None:
      return []
    self.serializedState = []
    self.postTraversal(self.serializerHelper)
    return self.serializedState

  def serializerHelper(self, item):
    if(item.__class__.__name__ == "Point"):
      self.serializedState.append(item)

  def search(self, point):
    return self.root.search(point)

  def generate_tree(self, node, point):
    leaf1 = Node(None, None, node.data)
    leaf2 = Node(None, None, point)
    leaf3 = Node(None, None, node.data)
    inner_node2 = Node(leaf2, leaf3, Segment(point, node.data))
    inner_node1 = Node(leaf1, inner_node2, Segment(node.data, point))
    return Tree(inner_node1)

  def insert(self, point):
    if self.root == None: 
      self.root = Node(None, None, point)
      return
    insert_node = self.search(point)
    new_tree = self.generate_tree(insert_node, point)
    insert_node.insert(new_tree)
