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

	def valueOfRange(self, nodes, min, max):
		for key in listofnodes:
		    node = self._bstSearch(self._root, key)
		    if node.value.key> min and node.value.key<max:
		         dict[node.value.key] = node.value.value
		         assert node is not None, "Invalid map key."
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
		elif subtree.key > min:
			listofnodes.append(subtree.key)
			return self._bstSearchRange(subtree.left, min, max)
		elif subtree.key < max:
			listofnodes.append(subtree.key)
			return self._bstSearchRange(subtree.right, min, max)
		return listofnodes

class _BSTMapNode :
	def __init__( self, key, value ):
		self.key = key
		self.value = value
		self.left = None
		self.right = None

prices = []
treemap = BSTMap()
treenode = _BSTMapNode(1,2)
treenode2 = _BSTMapNode(2,22)
treenode3 = _BSTMapNode(3,27)
treenode4 = _BSTMapNode(4,28)
treenode5 = _BSTMapNode(5,20)
treenode6 = _BSTMapNode(20,20)


treemap.add(1,treenode)
treemap.add(2,treenode2)
treemap.add(3,treenode3)
treemap.add(4,treenode4)
treemap.add(5,treenode5)
treemap.add(6,treenode3)
treemap.add(7,treenode2)
treemap.add(8,treenode4)
treemap.add(9,treenode5)
treemap.add(10,treenode6)


#print("size: " + str(treemap.size))
#pricerange = []

nodesinrangelist = treemap._bstSearchRange(treemap._root, 9, 11)
dictionaryofvalues = treemap.valueOfRange(nodesinrangelist, 0, 5)
print(listofnodes)
print(dictionaryofvalues)
