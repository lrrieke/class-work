from collections import OrderedDict

glossary = OrderedDict()

glossary['key-value pair'] = 'set of values associated with each other'
glossary['dictionary'] = 'collection of key-value pairs'
glossary['tuple'] = 'immutable list'

for word, definition in glossary.items():
	print("\n" + word.title() + ": " + definition)