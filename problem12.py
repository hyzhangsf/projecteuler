# https://projecteuler.net/problem=12
def f(n):
	# f(1) = 1
	# f(2) = 3
	return (1+n)*n/2

def divisor_count(n):
	return len( filter(lambda x:n%x==0, range(1, int((n+1)**0.5))))*2


assert divisor_count(28) == 6


from itertools import count
for i in count(1):	
	if divisor_count(f(i)) > 500:
		print f(i)
		break

	