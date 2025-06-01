import string
import time
from collections import deque

def collatz(n):
	parity = []
	while n != 1:
		parity.append('1' if n % 2 else '0')
		if n % 2 == 0:
			n = n // 2
		else:
			n = 3 * n + 1
	return ''.join(parity)


def reverse_from_parity(parity_str, final=1):
	n = final
	for bit in reversed(parity_str):
		if bit == '0':
			n = n * 2
		elif bit == '1':
			if (n - 1) % 3 != 0:
				return None  
			prev = (n - 1) // 3
			if prev % 2 == 0:
				return None  
			n = prev
		else:
			return None 
	return n

def generate_sequence(data):
	seq = []
	alpha = list(string.ascii_lowercase)
	for char in data.lower():
		if char in alpha:
			seq.append(alpha.index(char))
	return seq

def consume_sequence(sequence):
	str = []
	alpha = string.ascii_lowercase
	for s in sequence:
		if 0 <= s < len(alpha):
			str.append(alpha[s])
			
	return str

def encrypt(sequence):
	encrypted_string = []
	parity = []
	for num in sequence:
		par = collatz(num)
		encrypted_string.append(1)
		parity.append(par)
	return encrypted_string, parity

def decrypt(encrypted, parity):
	sequence = []
	for i, x in zip(encrypted, parity):
		n = reverse_from_parity(x, final = i)
		sequence.append(n)

	decrypted = consume_sequence(sequence)
	return "".join(str(n) for n in decrypted)


def main():
	string = "hello world"
	sequence = generate_sequence(string)
	
	encrypted_string, parity = encrypt(sequence)
	print("Encrypted String: " + "".join(str(n) for n in encrypted_string))
	print("-".join(parity))

	print("---------------------------------------------------------")
    
	decrypted_string = decrypt(encrypted_string, parity)
	print(decrypted_string)

if __name__ == "__main__":
	main()
