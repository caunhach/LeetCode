class BTree:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None
	def PrintTree(self, index):
		left = self.left
		right = self.right
		if self:
			print("index: ", index, end=" ")
			print("value: ", self.val)
		if left:
			left.PrintTree(index * 2)
		if right:
			right.PrintTree(index * 2 + 1)
	def InvertTree(self):
		if self:
			new = BTree(self.val)
			if self.left:
				new.right = self.left.InvertTree()
			if self.left:
				new.left = self.right.InvertTree()
		else:
			new = None
		return new

tree = BTree(4)
tree.left = BTree(2)
tree.right = BTree(7)
tree.left.left = BTree(1)
tree.left.right = BTree(3)
tree.right.left = BTree(6)
tree.right.right = BTree(9)
tree.PrintTree(1)
print("")
tree.InvertTree().PrintTree(1)

tree = BTree(2)
tree.left = BTree(1)
tree.right = BTree(3)
tree.PrintTree(1)
print("")
tree.InvertTree().PrintTree(1)