# https://projecteuler.net/problem=10

def primes():
	prime = []
	last = 2
	while True:
		for p in prime:
			if last % p ==0:
				break

		else:
			yield last
			prime.append(last)
		last += 1


sum = 0
for i in prime():
	if i < 2000000:
		sum += i
		print i
	else:
		break
print sum		