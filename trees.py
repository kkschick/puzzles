class Node(object):
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

class Tree(object):
	def __init__(self):
		self.root = None

	def search(self, value):
		node = self.root
		while node:
			if value < node.value:
				node = node.left
			elif value > node.value:
				node = node.right
			else:
				return node
		return "Not Found"

# Write your own binary search tree class and tree nodes
# Initialize said BST and append to it (ignore duplicate values)
# Once you've appended nodes in the right spots, print their values in order with the help of Whiteboarding/Trees01 exercise
# Research other kinds of trees, like heaps and red-black trees