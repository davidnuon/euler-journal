#!/usr/bin/env python

from common import *

def main():
	p = lambda k : 6 * k + 1
	np = lambda k : 6 * k - 1


	a = set([p(n) for n in xrange(1000000)])
	b = set([np(n) for n in xrange(1000000)])

	print map(isprime, list(a ^ b))
if __name__ == '__main__':
	main()