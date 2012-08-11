#!/usr/bin/env python

# This runs way too long, need to fix

from common import *

def tri():
	i = 1
	while True:
		yield (i*(i-1))/2
		i += 1

def main():
	tr = tri()
	for n in tr:
		if len(divisors(n)) > 500:
			print n
			
if __name__ == '__main__':
	main() 