#!/usr/bin/env python

from common import *

def main():
	n = 600851475143
	print max(n for n in factors(n) if isprime(n))

if __name__ == '__main__':
	main()