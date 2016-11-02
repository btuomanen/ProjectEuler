import functools
import  math

def trinum(n):
	y = functools.reduce(lambda x, y : x+y, range(1,n+1))
	return y

def numdivisors(n):
	numdivisors=0
	for i in range(1,math.floor(n/2)+1):
		if(n % i == 0):
			numdivisors +=1

	return(numdivisors)

numdiv = 0
curnum = 1
while (numdiv < 500):
	curnum += 1
	numdiv = numdivisors(trinum(curnum))

print(trinum(curnum))
	
	
