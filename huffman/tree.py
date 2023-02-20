
class Tree:
	def __init__(self, value:int, char: str = None, left = None, right = None):
		self.value = value
		self.char = char

		self.left = left
		self.right = right
	
	def is_leaf(self):
		return self.left is None and self.right is None

	def __repr__(self):
		default = str(self.value) + '\n'
		if self.right and self.left:
			default += "  " + repr(self.right) + "\n"
			default += "  " + repr(self.left) + "\n"
		return default

