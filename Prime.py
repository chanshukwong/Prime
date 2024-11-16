# Prime number within a range 
from math import sqrt
import numpy as np

max_n = 3
is_prime = np.zeros(max_n, dtype=bool)

def init_prime(n):
	global is_prime, max_n
	if n > max_n:
		is_prime[2]=False
		is_prime.resize(n)
		is_prime[max_n+(max_n%2==0)::2]=True
		for p in np.nonzero(is_prime[:int(sqrt(n+0.5)+1)])[0]:
			if is_prime[p]:
				is_prime[max(p*p, max_n)::p*2]=False
		max_n=n
	is_prime[2]=True

def prime_in_range(n, m=0):
	mx, nx = max(m, n), min(m, n)
	init_prime(mx)
	yield from np.nonzero(is_prime[nx:mx])[0]+nx

if __name__ == "__main__":
	for p in prime_in_range(400, 300):
		print(p, end=' ')
	print()

	for p in prime_in_range(100):
		print(p, end=' ')
	print()
