#!/usr/bin/env python

from common import *

def main():
	n = 2
	limit = 4000000
	
	while fib(n) < limit:
		n += 1

	print sum(fib(i) for i in xrange(2, n) if fib(i) % 2 == 0)

if __name__ == '__main__':
	main()