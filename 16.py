import math
import functools
import sys
f = open('13data.txt','r')
a = f.readline()
numberz = []

while(a != ''):
	numberz.append (int(a))
	a = f.readline()

s = (sum(numberz))

powa = math.floor(math.log(s,10))
	
n = 0
nums = []
s1=s
for i in range(0,int(powa)+1):
	nums.append(s % 10)
	s = int(s / 10)

for i in range(1,11):
	sys.stdout.write(str(nums[-i]))
print('')
print(s1)
