import functools

def readData():
	f = open('8data.txt','r')
	data = f.read()
	numberz = []
	
	for c in data:
		i = ord(c) - ord('0')
		if( 0 <= i and i <= 9):
			numberz.append(i)
	return (numberz)
			
def mult13(n, nums):
	y=functools.reduce(lambda x, y: x*y, nums[n:n+13])
	return y

	
numz = readData()
valz = []
for i in range(1000 - 13):
	valz.append(mult13(i,numz))

print(max(valz))	
