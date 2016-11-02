import math

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

primes = buildprimes(2000000)
sum(primes)