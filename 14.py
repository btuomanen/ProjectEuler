def collatz(n):
	collatz_chain=[n]
	while ( n != 1):
		if(n % 2 == 1):
			n = 3*n + 1
		else:
			n = n/2
		collatz_chain.append(n)
	return ( len(collatz_chain) )

max1 = 0
ind1 = 1
for x in range(1,1000000 + 1):
	m = collatz(x)
	if(m > max1):
		max1 = m
		ind1 = x
print(max1)
print(ind1)
