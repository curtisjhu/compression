

if __name__ == "__main__":
	pass

#### https://youtu.be/h0jloehRKas
### https://youtu.be/X8jsijhllIA
### https://youtu.be/b3NxrZOu_CE

def get_packets(secret:int):

	# n pairs uniquely determine a n-1 polynomial
	pairs = []
	while secret:
		pairs += secret % 10
		secret = secret // 10
	
	# convert into a polynomial


	# from polynomial we find k additional pairs to account for k general errors


def randomly_alter_secret(secret:int, k):
	# Randomly flips and changes our secret

	pass

def decode_packets(altered_secret:int):
	pass

	
