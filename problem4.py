# https://projecteuler.net/problem=4
# Largest palindrome product
from itertools import product as p
isPalindrome = lambda n: str(n) == str(n)[::-1]
print max( filter(isPalindrome,  map(lambda (x,y):x*y, p(range(100, 999), range(100, 999)))) )



