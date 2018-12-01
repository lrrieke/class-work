favorite_places = {
	'patrick' : ['sweden', 'norway', 'scotland'],
	'lena' : ['london', 'paris', 'barcelona'],
	'renee' : ['cabo san lucas', 'catalina', 'monterey']
	}

for name, places in favorite_places.items():
	print("\n" + name.title() + "'s favorite places are: ")
	for place in places:
		print("\t" + place.title())