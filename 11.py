import functools

def read_by_tokens(fileobj):
    for line in fileobj:
        for token in line.split():
            yield token

def readData():
	numberz = []
	f = open('11data.txt')	
	tokenz = read_by_tokens(f)
	for c1 in tokenz:
		numberz.append(int(c1))
	return (numberz)
			

def multd(n, nums):
	y=functools.reduce(lambda x, y: x*y, nums[n:n+21*3+1:21])
	return y

def multd2(n, nums):
	y = functools.reduce(lambda x, y: x*y, nums[n:n+19*3+1:19])
	return y

def multh(n,nums):
	print(nums[n:n+4])
	y=functools.reduce(lambda x, y: x*y, nums[n:n+4])
	print(y)
	return y

def multv(n,nums):
	y=functools.reduce(lambda x, y: x*y, nums[n:n+20*3+1:20])
	return y	

	
numz = readData()
vald = []
valv = []
vald2 = []
valh = []
for i in range(400 - 3*21):
	vald.append(multd(i,numz))
for i in range(400 - 3):
	valh.append(multh(i,numz))
for i in range(400 - 3*20):
	valv.append(multv(i,numz))
for i in range(3, 400 - 3*19):
	vald2.append(multd2(i,numz))
print(max(vald+valh+valv+vald2))	
