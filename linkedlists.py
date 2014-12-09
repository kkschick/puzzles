"""You are in a room with a circle of 100 chairs. The chairs are numbered sequentially from 1 to 100.

At some point in time, the person in chair #1 will be asked to leave. The person in chair #2 will be skipped, and the person in chair #3 will be asked to leave. This pattern of skipping one person and asking the next to leave will keep going around the circle until there is one person left the survivor.

Write a program to determine which chair the survivor is sitting in."""

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

	def PrintList(self):
		node = self.head

		while node != None:
			print node.data
			node = node.next

# Double linked list also has "previous" so you can go backward and forward