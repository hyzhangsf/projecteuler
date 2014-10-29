# https://projecteuler.net/problem=6
print abs(sum(map(lambda x: x**2, range(101))) - sum(range(101))**2)