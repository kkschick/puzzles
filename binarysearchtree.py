class BinarySearchTree(object):
	def __init__(self):
		self.root = None

	def append_node(self, new_node):
		if self.root == None:
			self.root = new_node
		else:
			node = self.root
			while node:
				if (new_node.data < node.data) and node.left:
					node = node.left
				elif (new_node.data > node.data) and node.right:
					node = node.right
				elif (new_node < node.data):
					node.left = new_node
					return
				elif (new_node > node.data):
					node.right = new_node
					return
