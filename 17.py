#!/usr/bin/env python

digits = { 
	'1' : 'one',
	'2' : 'two',
	'3' : 'three',
	'4' : 'four',
	'5' : 'five',
	'6' : 'six', 
	'7' : 'seven',
	'8' : 'eight',
	'9' : 'nine',
	'10' : 'ten',
	'11' : 'eleven',
	'12' : 'twelve', 
	'13' : 'thirteen',
	'14' : 'fourteen',
	'15' : 'fifteen',
	'16' : 'sixteen',
	'17' : 'seventeen',
	'18' : 'eighteen',
	'19' : 'nineteen',
	'20' : 'twenty',
	'30' : 'thirty',
	'40' : 'forty',
	'50' : 'fifty', 
	'60' : 'sixty', 
	'70' : 'seventy',
	'80': 'eighty',
	'90': 'ninety',
}

prefix = {
	'h': 'hundred',
	't': 'thousand' 
}

def wordLength(n):
	key = str(n)

	if key in digits:
		return len(digits[key])

def main():
	c = 0

	# Generate 20 - 99
	for n in xrange(20, 100, 10):
		for k in xrange(n + 1, n+10):
			key = str(k)
			if not key in digits:
				tens = str(k/10 * 10)
				units = str(k % 10)
				digits[key] = digits[tens] + digits[units]

	# Generate 100 to 1000
	for n in xrange(100, 1000, 100): 
		for k in xrange(n, n+100):
			key = str(k)
			hundreds = str(k/100)
			tens     = str(k%100)

			if tens == '0':
				digits[key] = digits[hundreds] + prefix['h']
				continue

			digits[key] = digits[hundreds] + prefix['h'] + 'and' + digits[tens]

	# Don't forget to add 100
	digits['1000'] = digits['1'] + prefix['t']

	print sum([len(digits[n]) for n in digits])

if __name__ == '__main__':
	main()  