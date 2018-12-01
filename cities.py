cities = {
	'las vegas' : {
		'country' : 'united states',
		'population' : '2000000',
		'fact' : 'The Las Vegas Strip is the brightest place on Earth when viewed from outer space.'
		},
	'nice'	: {
		'country' : 'france',
		'population' : '1000000',
		'fact' : 'Nice is the fifth most populous city in France.'
		},
	'cardiff' : {
		'country' : 'wales',
		'population' : '350000',
		'fact' : 'Cardiff was once the richest city in the world.'
		}	
	}

for city, city_info in cities.items():
	print(city.title())
	country = city_info['country']
	population = city_info['population']
	fact = city_info['fact']

	print("\nCounty: " + country.title())
	print("\nPopulation: " + population)
	print("\nFact: " + fact)