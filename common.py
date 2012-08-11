import math

def fib(n, l = {}):
	if n in (0, 1):
		return n
	else:
		nkey = str(n)
		if nkey in l:
			return l[nkey]
		else:
			l[nkey] = fib(n - 1, l) + fib(n - 2, l)
			return l[nkey]

def factors(n):
	position = 1
	outs = []

	while position <= n:
		if n % position == 0:
			n /= position
			outs.append(position)
		position += 1

	return outs

def divisors(n):
	outs = set([])
	factors = []
	s = []

	for x in xrange(2, int(math.sqrt(n))):
		if n % x == 0:
			outs.add(n)
			outs.add(x)

	factors = list(outs)

	for x in factors:
		for y in factors:
			key = x * y
			if n % key == 0 and key < n:
				outs.add(key)
 
	outs.add(1)
	return list(outs)

def isprime(n):
	prime = True
	if n < 2:
		return False

	if n == 2:
		return True
	
	for k in xrange(2, int(math.sqrt(n)) + 1):
		if n % k == 0:
			return False

	return prime