from pylab import *

sum = 0

for n in range(1,1000,1):
	if ( (n % 5) == 0 or (n % 3) == 0 ):
		sum += n

print( sum )
