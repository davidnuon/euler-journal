#!/usr/bin/env python

def palindrome(n):
	s = str(n)
	return s == s[::-1]

def main():
	table = {}
	a = range(100, 1000)
	b = range(100, 1000)

	for j in a:
		for k in b:
			# For any n in [100, 999], palindrome(n*n) is False
			# so we need not compute it
			if j == k:
				continue
			else:
				key = str(sorted([j, k]))
				
				# If the key is stored, we need not compute it.
				if key in table:
					continue
				else:
					table[key] = j * k

	print max([table[n] for n in table if palindrome(table[n])])
if __name__ == '__main__':
	main()