# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
		node = BST(value)
		tree = self
		while True:
			if value >= tree.value:
				if tree.right:
					tree = tree.right
				else:
					tree.right = node
					break
			elif value < tree.value:
				if tree.left:
					tree = tree.left
				else:
					tree.left = node
					break
        return self

    def contains(self, value):
        # Write your code here.
		tree = self
		while tree:
			if tree.value == value:
				return True
			elif tree.value > value:
				tree = tree.right
			elif tree.value < value:
				tree = tree.left
		return False

    def remove(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
		tree = self
		r_tree = None
		l_tree = None
		parent_node = self
		while tree:
			if tree.value == value:
				right = tree.right
				left = tree.left
				if right and left:
					while right.left:
						parent_node = right
						right = right.left
					parent_node.left = right.right
					right.right = tree.right
					right.left = left
					self = right
				elif left and not right:
					parent_node.right = left
				elif right and not left:
					parent_node.left = right
				break
			elif tree.value > value:
				parent_node = tree
				tree = tree.right
				break
			elif tree.value < value:
				parent_node = tree
				tree = tree.left
				break
				
        return self

