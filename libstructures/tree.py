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
      return self.data
    else:
      if(direction(self.data, point) == 'left'):
        return self.left.search(point)
      else:
        return self.right.search(point)

class Tree:
  def __init__(self, root):
    self.root = root

  def postTraversal(self, visitor):
    self.root.postTraversal(visitor)

  def serialize(self):
    self.serializedState = []
    self.postTraversal(self.serializerHelper)
    return self.serializedState

  def serializerHelper(self, item):
    if(item.__class__.__name__ == "Point"):
      self.serializedState.append(item)

  def search(self, point):
    return self.root.search(point)
