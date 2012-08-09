#!/usr/bin/env python

def main():
	position = 2520
	
	while not all([bool(position % n == 0) for n in xrange(1, 21)]):
		position += 2520

	print position
if __name__ == '__main__':
	main()
