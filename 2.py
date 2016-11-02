from pylab import *

# fibonacci
def fib0(n):
	if n > 2:
		return ( fib0(n-2)+fib0(n-1) )
	elif n == 2:
		return ( 2 )
	elif n == 1:
		return ( 1) 

sum = 0
n = 1
fibo = fib0(n)
while fibo < 4000000:
	if fibo % 2 == 0: 
		sum += fibo
	n += 1
	fibo = fib0(n)

print(sum)

