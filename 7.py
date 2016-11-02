import math
import numpy

def checkprime(x, primes):
	for y in primes:
		if x % y == 0:
			return False
	
	return True

def buildprimes(N):
	primes = [2]
	j = 1
	i = 3
	while (j < N):
		if(checkprime(i,primes)):
			primes.append(i)
			j += 1
		i += 2
		

	return primes

def primepower(p,x):
	n = 0
	
	while ( x % p == 0):
		n += 1
		x /= p
	
	return n



primes = buildprimes(10001)

print (max(primes))

	
	