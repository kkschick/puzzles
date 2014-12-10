class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None
		self.tail = None

	def AddNode(self, data):
		new_node = Node(data)

		if self.head == None:
			self.head = new_node

		if self.tail != None:
			self.tail.next = new_node

		self.tail = new_node

	def RemoveNode(self, location):
		prev = None
		node = self.head
		counter = 0

		while (counter < location) and (node != None):
			prev = node
			node = node.next
			counter += 1

		if prev == None:
			self.head = node.next
		else:
			prev.next = node.next

	def PrintList(self):
		node = self.head

		while node != None:
			print node.data
			node = node.next

# Double linked list also has "previous" so you can go backward and forward