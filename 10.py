#!/usr/bin/env python

from common import *

def main():
	allnumbers = set(range(0, 2000000))
	firstprimes = set([2,3,5,7,13,17,19,23])

	for n in firstprimes:
		allnumbers = allnumbers - set(xrange(n, 2000000, n))

	print sum([n for n in allnumbers | firstprimes if isprime(n)])
if __name__ == '__main__':
	main()