# https://projecteuler.net/problem=2

dictionary = {0:1, 1:1}
def fibo():
	a, b, c = 1, 1, 0
	sum = 0
	while c<4000000:
		c = a + b
		a, b = b, c
		if c % 2 == 0:
			sum += c
			print c
	return sum

print fibo()			

