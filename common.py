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

def isprime(n):
	prime = True

	if n < 2 or n % 2 == 0:
		return False
	
	for k in xrange(2, n - 1):
		if n % k == 0:
			prime = False

	return prime