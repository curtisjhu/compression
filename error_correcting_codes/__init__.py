import random
import math

if __name__ == "__main__":
	pass

#### https://youtu.be/h0jloehRKas
### https://youtu.be/X8jsijhllIA
### https://youtu.be/b3NxrZOu_CE

def get_packets(secret:int):

	# n pairs uniquely determine a n-1 polynomial
	pairs = []
	p = 1
	while secret:
		rem = secret % 10
		pairs.insert(0, rem)

		p *= rem
		secret = secret // 10

	p += 1
	
	# convert into a polynomial
	deltas = []
	for a in pairs:
		numerator = lambda x: math.prod([x - b for b in pairs if b != a])
		denominator = math.prod([a - b for b in pairs if b != a])
		inverse = pow(denominator, p-2, p)
		deltas.append(lambda x: inverse * numerator(x))

	original_pairs = list(pairs)
	def polynomial(x):
		delta_sum = 0
		for i, y in enumerate(original_pairs):
			delta_sum += y*deltas[i](x)
		return delta_sum

	# from polynomial we find k additional pairs to account for k general errors
	k = int(2 * (len(pairs) / 2))
	for i in range(len(original_pairs)):
		pairs.append(polynomial(i))

	return pairs



def randomly_alter_message(message, k):
	# Randomly flips and changes our secret
	num_of_changes = random.randint(0, k)
	num_of_erases = random.randint(num_of_changes, k)

	for _ in num_of_changes:
		i = random.randint(len(message))
		message[i] += random.randint(-5, 5)
	
	for _ in num_of_erases:
		i = random.randint(len(message))
		message.pop(i)

	return message

def decode_packets(altered_secret:int):
	pass

	
