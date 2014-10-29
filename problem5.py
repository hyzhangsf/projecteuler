# https://projecteuler.net/problem=5
from fractions import gcd
print reduce(lambda x,y: x*y/gcd(x, y), range(1,21))