import math

def reversenumber(x):
	reverso = 0
	iters = math.floor(math.log(x,10))
	for i in range(1,iters+2,1):
		reverso *= 10
		remainder = x % 10
		reverso += remainder
		x /= 10
		x = math.floor(x)
	
	return (reverso)
		

palins = []

for i in range(1,1000):
	for j in range(1,1000):
		if(reversenumber(i*j) == i*j):
			palins.append(i*j)

print(max(palins))

