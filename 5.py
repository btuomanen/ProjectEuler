import math
import numpy

def checkprime(x, primes):
	for y in primes:
		if x % y == 0:
			return False
	
	return True

def buildprimes(r):
	primes = [2]
	for i in range(3,r+1):
		if(checkprime(i,primes)):
			primes.append(i)

	return primes

def primepower(p,x):
	n = 0
	
	while ( x % p == 0):
		n += 1
		x /= p
	
	return n



primes = buildprimes(20)
primepowers = []

for p in primes:
	curp = 0
	print('blah')
	maxp = 0
	for i in range(1,21,1):
		curp = max(primepower(p,i), curp)
		
	primepowers.append(curp)

thenumer = 1

for i in range(len(primes)):
	
	thenumer *= (primes[i] ** primepowers[i])

print (thenumer)
	
	