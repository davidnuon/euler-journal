#!/usr/bin/env python

# Naive implementation

def collatz(n):
	count = 1
	while n != 1:
		if n % 2 == 0:
			n /= 2
		else:
			n = 3*n + 1

		count += 1

	return count

def main():
	maxcollatz = {
		"length" : 2,
		"number" : 2
	}

	for n in xrange(2, 1000000):
		if collatz(n) > maxcollatz["length"]:
			maxcollatz["length"] = collatz(n)
			maxcollatz["number"] = n

	print maxcollatz

if __name__ == '__main__':
	main(), 