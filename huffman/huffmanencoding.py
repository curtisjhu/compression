import math
from .tree import Tree

def create_frequency_map(location):
	freq_map = {}

	with open(location, "r") as f:
		while(True):
			char = f.read(1)

			if not char:
				break

			if freq_map.__contains__(char):
				freq_map[char].value += 1
			else:
				freq_map[char] = Tree(1, char)
	
	return freq_map

def two_smallest(dictionary):
	min_freq = math.inf
	second_min_freq = math.inf
	min_char = ''
	second_min_char = ''
	for x in dictionary:
		curr = dictionary[x].value
		if curr < second_min_freq:
			if curr < min_freq:
				min_freq = curr
				min_char = x
			else:
				second_min_freq = curr
				second_min_char = x
	
	if not min_char or not second_min_char:
		return None, None
	return min_char, second_min_char 

def create_tree(fmap):

	# two smallest character (frequency wise)
	one, two = two_smallest(fmap)
	while(one and two):
		one_tree = fmap[one]
		two_tree = fmap[two]

		combined_freq = one_tree.value + two_tree.value
		node = Tree(combined_freq, left=one_tree, right=two_tree)
		
		hashcode = str(node.__hash__())
		fmap[hashcode] = node

		fmap.pop(one)
		fmap.pop(two)
		one, two = two_smallest(fmap)
	
	return list(fmap.values())[0]

def create_table(tree):
	code_table = {}

	codes = recurse_tree(tree, '')

	for pair in codes:
		code_table[pair[0]] = pair[1]

	return code_table

def recurse_tree(tree, code):
	if tree.is_leaf():
		return [(tree.char, code)]
	
	left_codes = recurse_tree(tree.left, code + '0')
	right_codes = recurse_tree(tree.right, code + '1')
	
	return left_codes + right_codes

def encode_document(file_input, file_output, table):
	with open(file_input, "r") as fin:
		with open(file_output, "w") as fout:
			while True: 
				c = fin.read(1)
				if not c:
					break
				fout.write(table[c] + " ")