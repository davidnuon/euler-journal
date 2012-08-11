#!/usr/bin/env python

# Binomial Coefficient
# Number of shortest paths in an nxn grid: 2n choose n

def combo(n, k):
	if k > (n-k):
		k = n - k
	c = 1

	for i in xrange(0, k):
		c *= (n-i)
		c /= (i+1)
	return c

def main():
	print combo(40, 20)

if __name__ == '__main__':
	main()