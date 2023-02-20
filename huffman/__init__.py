from .huffmanencoding import create_frequency_map, create_tree, create_table, encode_document
from .tree import Tree


def encode(file_input, file_output):
	m = create_frequency_map("input.txt")
	t = create_tree(m)
	table = create_table(t)
	encode_document(file_input, file_output, table)

	return table

def decode(file_input, file_output, table):
	keys = list(table.keys())
	vals = list(table.values())
	with open(file_input, "r") as fin:
		with open(file_output, "w") as fout:
			for x in fin.read().split(" "):
				if x:
					c = keys[vals.index(x)]
					fout.write(c)

