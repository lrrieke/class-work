def count_words(filename):

	try:
		with open(filename, encoding = 'utf-8') as file_object:
			contents = file_object.read()
	except FileNotFoundError:
		message = "Sorry, the file " + filename + " does not exist."
		print(message)
	else:
		words = contents.split()
		num_words = len(words)
		print("The file " + filename + " has about " + str(num_words) + " words.")

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
	count_words(filename)