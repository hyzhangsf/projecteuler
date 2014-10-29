d = dict()
def next(n):

	if n % 2 ==0:
		return n/2
	else:
		return n*3+1

def length(nn):
	if nn == 1: return 1
	size = 1
	new_n = nn
	while True:
		new_n = next(new_n)
		if new_n in d:
			d[nn] = d[new_n] + size
			return d[nn]
		size+= 1
		if new_n == 1:
			# d[nn] = size
			return size




assert length(2)==2
assert length(13)==10
from itertools import count
longest = (1,1)
for i in xrange(1,1000000):
	print i
	longest = max(longest, ( length(i),i))
print longest[1]
