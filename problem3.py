# https://projecteuler.net/problem=3
NUMBER = 600851475143
primes = set()
def isPrime(n):
	# for i in primes:
	# 	if n % i == 0:
	# 		primes.add(n)
	# 		print(n)
	# 		return False
	for i in range(1, int(n**0.5)+1):		
		if n % i == 0 and i != 1:
			primes.add(n)
			return False
	return True

assert isPrime(2)
assert isPrime(3)
assert not isPrime(4)
assert not isPrime(200)
assert isPrime(211)

print max(filter(isPrime, filter(lambda n: NUMBER%n == 0, range(1, int(NUMBER**0.5)+1))))

