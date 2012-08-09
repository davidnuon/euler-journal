#!/usr/bin/env python

from common import *

def main():
	k = 1
	n = 0

	while k < 10001:
		if isprime(n):
			k += 1
		n += 1
	print k, n

if __name__ == '__main__':
	main()