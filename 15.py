def countgrid(n,i):

	if(i == 0):
		return ( 1 )

	else:
		m = 0
		for j in range(0, n + 1):
			m += countgrid(j, i - 1)
		return (m)


print(countgrid(20,20))
