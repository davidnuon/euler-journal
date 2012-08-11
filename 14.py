#!/usr/bin/env python

table = {}

def collatz(n):

	if n == 0 or n == 1:
		return 1

	position = n
	count = 0

	while position != 1:
		key = str(position)
		if key in table:
			table[str(n)] = count + table[key]
			return table[str(n)]
		else:
			if position % 2 == 0:
				position /= 2
			else:
				position = 3*position + 1
			count += 1

	table[str(n)] = count
	return table[str(n)]

def main():
	maxcollatz = {
		"length" : 2,
		"number" : 2
	}

	for n in xrange(2, 1000000):
		if collatz(n) > maxcollatz["length"]:
			maxcollatz["length"] = collatz(n)
			maxcollatz["number"] = n

	print maxcollatz


if __name__ == '__main__':
	main()
