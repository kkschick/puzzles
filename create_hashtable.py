class HashTable(object):
	HASH_LENGTH = 10

	def __init__(self):
		self.list_of_lanes = []
		i = 0
		while i < self.HASH_LENGTH:
			self.list_of_lanes.append([])
			i += 1

	def set(self, key, value):
		hash_num = self.hash(key)
		self.list_of_lanes[hash_num].append((key,value))

	def get(self, key):
		hash_num = self.hash(key)
		lane = self.list_of_lanes[hash_num]
		for keyvalue in lane:
			if keyvalue[0] == key:
				return keyvalue[1]

	def hash(self, key):
		i = 0
		key_num = 0
		while i < len(key):
			key_num += ord(key[i])
			i += 1
		return key_num % self.HASH_LENGTH

hasht = HashTable()
hasht.set('apple', 5)
print hasht.get('apple')