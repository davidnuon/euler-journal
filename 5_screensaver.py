#!/usr/bin/env python

def main():
	divsors = range(1, 21)
	position = 2
	done = False

	while not done:
		test = map(int, [position % n == 0 for n in divsors])
		if not int(False) in test:
			done = True
		else:
			position += 2
		print position, ''.join(map(lambda x : ('-', '_')[int(x)], test))

if __name__ == '__main__':
	main()