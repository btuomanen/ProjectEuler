A1=[]
B1=[]
C1=[]
for c in range(3,1000,1):
	for b in range(2,c,1):
		for a in range(1, b,1):
			if(( a**2 + b**2 == c**2 ) and (a + b + c == 1000)):

				print(a)
				print(b)
				print(c)
				break

