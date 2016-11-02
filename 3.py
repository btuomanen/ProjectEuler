# from pylab import *
import math

def checkprime(x, primes):
	for y in primes:
		if x % y == 0:
			return False
	
	return True

# build a list of primes

def buildprimes(r):
	primes = [2]
	for i in range(3,r+1):
		if(checkprime(i,primes)):
			primes.append(i)

	return primes


l1 = buildprimes(math.floor(100000))
thenum= 600851475143 #<-- what is the largest prime that divides into this? 

dividesthenum = [1]

for i in l1:
	if(thenum % i == 0):
		dividesthenum.append(i)

print ( max(dividesthenum) )
