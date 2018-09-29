import random

dict = {}
listofnodes = []

class BSTMap:
	def __init__(self):
		self._root = None
		self._size = 0

	def add(self, key, value):
		node = self._bstSearch(self._root, key)
		if node is not None:
			node.value = value
			return False
		else:
			self._root = self._bstInsert(self._root, key, value)
			self._size += 1
			return True

	def _bstInsert(self, subtree, key, value):
		if subtree is None:
			subtree = _BSTMapNode(key, value)
		elif key < subtree.key:
			subtree.left = self._bstInsert(subtree.left, key, value)
		elif key > subtree.key:
			subtree.right = self._bstInsert(subtree.right, key, value)
		return subtree

	def valueOf(self, key):
		node = self._bstSearch(self._root, key)
		assert node is not None, "Invalid map key."
		return node.value

	def valueOfRange(self, nodes):
		for key in listofnodes:
			node = self._bstSearch(self._root, key)
			dict[key] = node.value
		return dict



	def _bstSearch(self, subtree, target):
		if subtree is None:
			return None
		elif target < subtree.key:
			return self._bstSearch( subtree.left, target)
		elif target > subtree.key:
			return self._bstSearch(subtree.right, target)
		else:
			return subtree

	def _bstSearchRange(self, subtree, min, max):
		if subtree is None:
			return None
		if subtree.key >= min and subtree.key <= max:
			listofnodes.append(subtree.key)
		self._bstSearchRange(subtree.right, min, max)
		self._bstSearchRange(subtree.left, min, max)
		return listofnodes

	def _bstMinimum( self, subtree ):
		if subtree is None :
			return None
		elif subtree.left is None :
			return subtree
		else :
			return self._bstMinimum( subtree.left )

	def _bstMaximum( self, subtree ):
		if subtree is None :
			return None
		elif subtree.right is None :
			return subtree
		else :
			return self._bstMaximum( subtree.right )

class _BSTMapNode :
	def __init__( self, key, value ):
		self.key = key
		self.value = value
		self.left = None
		self.right = None

numberslist = [60,25,100,35,17,80]

bst = BSTMap()
bst.add(5,"glasses")
bst.add(11,"strawberry")
bst.add(1,"shoes")
bst.add(10,"banana")
bst.add(7,"apple")
bst.add(2,"pants")
bst.add(3,"candy")
bst.add(9,"mango")

bst.add(6,"dress")
bst.add(4,"hat")
bst.add(8,"orange")
bst.add(13,"ball")


searchitem = bst._bstSearch(bst._root,5)
print("item found: " + searchitem.value)

min = bst._bstMinimum(bst._root) #searches for the minimum value in the bstmap
max = bst._bstMaximum(bst._root) #searches for the maximum value in the bstmap

print("min: " + min.value)
print("max: " + max.value)
print("root: " + bst._root.value)

minrange = 5  #enter minimum range to search
maxrange = 10 #enter maximum range to search
itemsinrange = bst._bstSearchRange(bst._root,minrange,maxrange) #searches for keys within the specified range
itemsinrange.sort() #sorts the list of items
valuesofitems = bst.valueOfRange(itemsinrange) #gets the keys and specified values in dictionary format

print("keys found in range: " + str(itemsinrange)) #prints the search results
print("item values: " + str(valuesofitems)) #prints the keys and values

