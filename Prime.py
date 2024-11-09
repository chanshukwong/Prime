# Prime number within a range 
from math import sqrt
import numpy as np

is_prime = np.array([0,0,1], dtype=bool)
max_n = len(is_prime)

def init_prime(n):
	global is_prime, max_n
	if n > max_n:
		is_prime.resize(n)
		is_prime[max_n+(max_n%2==0)::2]=True
		for i in range(3, int(sqrt(n+0.05)+1), 2):
			if is_prime[i]:
				is_prime[max(i*i, max_n)::i*2]=False
		max_n=n

def prime_in_range(n, m=0):
	mx, nx = max(m, n), min(m, n)
	init_prime(mx)
	yield from np.nonzero(is_prime[nx:mx])[0]+nx

if __name__ == "__main__":
	for p in prime_in_range(300, 500):
		print(p, end=' ')
	print()

	for p in prime_in_range(100):
		print(p, end=' ')
	print()
