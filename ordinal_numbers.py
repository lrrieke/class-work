numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

if number in numbers >= 1:
	print( str(number) + "st")
elif number in numbers >= 2:
	print( str(number) + "nd")
elif number in numbers >= 3:
	print (str(number) + "rd")
else:
	print( str(number) + "th")