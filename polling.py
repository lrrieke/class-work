favorite_languages = {
	'jen' : 'python',
	'sarah' : 'c',
	'edward' : 'ruby',
	'phil' : 'python',
}

names = ['erin', 'jen', 'john', 'sarah', 'edward', 'phil']

for name in names:
	if name in favorite_languages.keys():
		print("Thank you for taking the poll, " + name.title() + "!")
	else:
		print(name.title() + ", you should take the poll!")
