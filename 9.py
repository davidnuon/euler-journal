#!/usr/bin/env python

def main():

	for c in xrange(1, 1000):
		for b in xrange(1, c):
			for a in xrange(1, b):
				if a ** 2 + b **2 == c ** 2:
					if sum([a,b,c]) == 1000:
						print reduce(lambda a,b :a * b, [a,b,c])
						return

if __name__ == '__main__':
	main()