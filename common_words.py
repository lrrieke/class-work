def count_words(filename):

	try:
		with open (filename, encoding='utf-8') as file_object:
			contents = file_object.read()
	except FileNotFoundError:
		message = "Sorry, the file " + filename + " does not exist."
		print(message)
	else:
		words = contents.lower().split()
		num_words = words.count('the')
		print("The file " + filename + " has the word 'the' about " + str(num_words) + " times.")

filename = 'alice.txt'
count_words(filename)