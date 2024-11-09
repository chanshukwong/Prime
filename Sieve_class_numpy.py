# Create class Sieve from numpy
import sys
from math import sqrt
import numpy as np

class Sieve():
	def __init__(self, n):
		self.is_prime = np.ones(n, dtype=np.int8)
		self.is_prime[:2]=False
		self.is_prime[4::2]=False
		for i in range(3, int(sqrt(n+0.05)), 2):	# sub list start from 2, end at sqrt(n) 
			if self.is_prime[i]:
				self.is_prime[i*i::i*2]=False

	def __iter__(self):
		return iter(np.where(self.is_prime==True)[0])

	def __str__(self):								# Only work for small amount of primes
		np.set_printoptions(threshold=sys.maxsize)
		return str(np.where(self.is_prime==True)[0])

	def get_primes(self):
		for i in np.where(self.is_prime==True)[0]:
			yield i

	def get_nof_primes(self):
		return np.count_nonzero(self.is_prime) 

def main():
	# try:
	# 	num = int(sys.argv[1])
	# except IndexError as e:
	# 	sys.exit(f"Missing arguments: python {sys.argv[0]} last_number")	
	num = 1000000000
	# for v in Sieve(num+1):
	# 	print(v, end=' ')
	# print()
	# print(Sieve(num+1))	# if num is very big, it stucks.
	S=Sieve(num+1)
	for v in S.get_primes():
		print(v, end=' ')
	print(f"\nThe total number of primes is {S.get_nof_primes()}")

if __name__ == "__main__":
	main()
