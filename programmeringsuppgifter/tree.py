class Node():
  def __init__(self, data):
      self.data = data

class BinaryTree:
  def __init__(self, data):
    self.root = Node(data)
  
tree = BinaryTree(3)

print(tree.root.data)
