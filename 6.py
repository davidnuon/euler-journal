#!/usr/bin/env python

def main():
	space = xrange(0, 101)
	print sum(space)**2 - sum(n**2 for n in space)

if __name__ == '__main__':
	main()