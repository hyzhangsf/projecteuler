# https://projecteuler.net/problem=9
def fun():
	for c in xrange(1000):
		for a in xrange(1000):
				b = 1000 - a - c
				if a+b+c==1000 and a*a + b*b == c*c:
					return a*b*c

print fun()