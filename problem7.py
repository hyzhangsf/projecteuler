# https://projecteuler.net/problem=7
def isPrime(n):
	# for i in primes:
	# 	if n % i == 0:
	# 		primes.add(n)
	# 		print(n)
	# 		return False
	for i in range(1, int(n**0.5)+1):		
		if n % i == 0 and i != 1:
			return False
	return True

i = 2
count = 0

while True:
	if isPrime(i):
		count += 1
		if count == 10001:
			print i
			break
		
	i += 1
