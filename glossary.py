from collections import OrderedDict

glossary = OrderedDict()

glossary['key-value'] = 'set of values associated with each other'
glossary['dictionary'] = 'collection of key-value pairs'
glossary['tuple'] = 'immutable list' 

for key, definition in glossary.items():
	print(key.title() + ": " + definition())