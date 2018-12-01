favorite_numbers = {
	'patrick' : [7, 150, 13],
	'lena' : [23, 42, 2],
	'renee' : [143, 8, 10]
	}

for name, numbers in favorite_numbers.items():
	print("\n" + name.title() + "'s favorite numbers are:")
	for number in numbers:
		print("\t" + str(number))